from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django_countries import countries
from tourneys.models import *
from django.contrib.auth.models import User
from django_countries.fields import Country
from django.core.exceptions import ObjectDoesNotExist
import helpers
import datetime
from time import strptime
from django.utils import timezone
from math import *

#----------------------------------------------------------------------------------------
#--------------------------------------- INDEX ------------------------------------------
#----------------------------------------------------------------------------------------

def index(request):
	return render(request, 'tourneys/home.html')

#----------------------------------------------------------------------------------------
#---------------------------------- TOURNEYS METHODS -------------------------------------
#----------------------------------------------------------------------------------------

def my_tourneys(request):
	try:
		var_filter = request.GET.get('filter')
		tourneys = None
		user = User.objects.get(username=request.user)
		if var_filter == 'all':
			tourneys = Tourney.objects.filter(Finished=False)
		elif var_filter == 'mine':
			user_tourney = User_Tourney.objects.filter(Id_user=user)
			tourneys = [ x.Id_tourney for x in user_tourney if not x.Id_tourney.Finished ]
		elif var_filter == 'category':
			tourneys = Tourney.objects.filter(Console=request.GET.get('console'))

	except ObjectDoesNotExist:
		return render(request, "tourneys/my_tourneys.html", { 'consoles' : ['XBOX ONE', '3DS', 'WII U', 'PLAYSTATION 4'] });

	return render(request, "tourneys/my_tourneys.html", { 'consoles' : ['XBOX ONE', '3DS', 'WII U', 'PLAYSTATION 4'], 'tourneys' : tourneys });

def add_tourney(request):
	try:
		user = User.objects.get(username=request.user)
		date = helpers.getDateFromString( request.POST.get('start_date') )
		check_in = False if request.POST.get('check_in') == 'false' else True
		tourney = Tourney(Owner=user, Name=request.POST.get('name'), Game=request.POST.get('game'), Max_participants=request.POST.get('max_participants'), Creation_date=datetime.datetime.now() - datetime.timedelta(hours=6), Console=request.POST.get('console'), Start_date=date, Periodicity=request.POST.get('periodicity'), Check_in=check_in)
		tourney.save()
	except ObjectDoesNotExist:
		return HttpResponse('User does not exists')

	return HttpResponse(tourney.id)

def view_tourney(request, tourney_id):
	try:
		#get user and tourney objects
		user = User.objects.get(username=request.user)
		tourney = Tourney.objects.get(id=tourney_id)
		#check if the current user is the owner of the tourney
		is_owner = True if request.user == tourney.Owner else False
		#get the users sign up in the tourney
		participants = User_Tourney.objects.filter(Id_tourney=tourney_id)
		number_participants = len(participants)
		#check if the user is registered in the tourney
		is_registered = True if len( User_Tourney.objects.filter(Id_tourney=tourney_id, Id_user=user) ) > 0 else False
		#check if the tournament is full
		full = number_participants == tourney.Max_participants
		#get today and tournament date
		today = datetime.datetime.now() - datetime.timedelta(hours=6)
		tourney_date = tourney.Start_date.astimezone(timezone.utc).replace(tzinfo=None)
		#check if the tournament has started
		has_started = today > tourney_date
		#get the number of rounds
		n_rounds = int(ceil(log(number_participants, 2)))
		#boolean value for creating matchs
		create_match = not tourney.Created_rounds
		#check if the tournament has started and send the tournament user registered and their codes
		if has_started:
			codes = { x.Id_user.username : Code.objects.get(Id_user=x.Id_user, Console=tourney.Console) for x in participants}
			if not tourney.Created_rounds:
				createRounds(tourney, n_rounds)
		#get the final round value, cause of the bracket plugin

	except ObjectDoesNotExist:
		return HttpResponse("Tourney not found")

	return render(request, "tourneys/tourneys.html", { 'tourney' : tourney, 'is_owner' : is_owner, 'registered_count' : number_participants, 'tourney_id' : tourney_id, 'is_registered' : is_registered, 'participants' : participants, 'is_full' :  full, 'has_started' : has_started, 'codes' : codes, 'num_rounds' : n_rounds, 'create_matchs' : create_match})

def createRounds(tourney, n_rounds):
	for i in range(n_rounds):
		createRound(tourney, i + 2 if i == n_rounds - 1 else i)
	tourney.Created_rounds = True
	tourney.save()
	return True

def isRoundCreated(tourney, n_round):
	o_round = Round.objects.filter(Id_tourney=tourney)
	if o_round is None:
		return False
	return o_round.Round_number == n_round

def isRoundFinished(tourney, n_round):
	o_round = Round.objects.filter(Id_tourney=tourney, Round_number=n_round)
	matchs = Match.objects.filter(Id_round=o_round)
	for match in matchs:
		if match.Id_Winner is None:
			return False
	return True

#create round method
def createRound(tourney, n_round):
	o_round = Round(Id_tourney=tourney, Round_number=n_round, Start_date=tourney.Start_date + datetime.timedelta(minutes=tourney.Periodicity * n_round), End_date=tourney.Start_date + datetime.timedelta(minutes=tourney.Periodicity * (n_round + 1)))
	o_round.save()
	return True

#create match
def createMatch(request):
	tourney_id = request.POST.get('tourney_id')
	round_number = int(request.POST.get('round_number'))
	tourney = Tourney.objects.get(id=tourney_id)
	o_round = Round.objects.get(Id_tourney=tourney, Round_number=round_number)
	match = Match(Id_round=o_round, Match_number=int(request.POST.get('match_number')), Match_Pointer=int(request.POST.get('match_pointer')))
	match.save()
	username_1 = request.POST.get('username_1')
	username_2 = request.POST.get('username_2')
	arrive_time = o_round.Start_date + datetime.timedelta(minutes=5)
	addUserToMatch(match, username_1, username_2, arrive_time)
	return HttpResponse()

def addUserToMatch(match, username_1, username_2, arrive_time):
	if username_1 != "":
		user_1 = User.objects.get(username=username_1)
		user_1_match = User_Match(Id_match=match, Id_user=user_1, Arrive_time=arrive_time)
		user_1_match.save()
	if username_2 != "":
		user_2 = User.objects.get(username=username_2)
		user_2_match = User_Match(Id_match=match, Id_user=user_2, Arrive_time=arrive_time)
		user_2_match.save()
	return True

def sign_up(request):
	try:
		tourney_id = request.POST.get('tourney_id')
		tourney = Tourney.objects.get(id=tourney_id)
		user = User.objects.get(username=request.user)
		code = Code.objects.filter(Id_user=user, Console=tourney.Console)
		if len(code) <= 0:
			return HttpResponse("False")
		register_user = User_Tourney(Id_tourney=tourney, Id_user=user)
		register_user.save()
	except ObjectDoesNotExist:
		return HttpResponse("Tourney or User not found")

	return HttpResponse("Success")


#----------------------------------------------------------------------------------------
#---------------------------------- PROFILE METHODS -------------------------------------
#----------------------------------------------------------------------------------------

def profile(request):
	try:
		user = User.objects.get(username=request.user)
		user_profile =  User_Profile.objects.get(user=user)
		codes = Code.objects.filter(Id_user=user)
		consoles = [x.Console for x in codes ]
		console_list = [x for x  in  ['XBOX ONE', '3DS', 'WII U', 'PLAYSTATION 4'] if x not in consoles ]
	except ObjectDoesNotExist:
		return render(request, 'tourneys/profile.html')

	return render(request, 'tourneys/profile.html', { 'countries' : list(countries), 'country' : user_profile.country.code, 'codes' : codes , 'consoles' :  console_list})

def save_profile(request):
	try:
		user_pro = User_Profile.objects.get(user=User.objects.get(username=request.POST.get('user')))
		user_pro.country = Country(code=request.POST.get('country'), flag_url='/flags/' + request.POST.get('country') + '.gif')
		user_pro.save()
	except ObjectDoesNotExist:
		return HttpResponse('User does not exists')

	return HttpResponse("Success")

def add_console(request):
	try:
		user = User.objects.get(username=request.user)
		code = Code(Id_user=user, FC=request.POST.get('friendcode'), Nickname=request.POST.get('nickname'), Console=request.POST.get('console'))
		code.save()
	except ObjectDoesNotExist:
		return HttpResponse('User does not exists')

	return HttpResponse("Success")

def edit_console(request):
	try:
		user = User.objects.get(username=request.user)
		consoles = request.POST.getlist('consoles[]')
		friendcodes = request.POST.getlist('friendcodes[]')
		nicknames = request.POST.getlist('nicknames[]')
		for x in range(len(consoles)):
			code = Code.objects.get(Id_user=user, Console=consoles[x])
			code.FC = friendcodes[x]
			code.Nickname = nicknames[x]
			code.save()
	except ObjectDoesNotExist:
		return HttpResponse('User does not exists')

	return HttpResponse("Success")
