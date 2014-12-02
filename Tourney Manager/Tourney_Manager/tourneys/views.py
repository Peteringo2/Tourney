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
		if var_filter == 'all':
			tourneys = Tourney.objects.filter(Finished=False)
		elif var_filter == 'mine':
			tourneys = Tourney.objects.filter(Finished=False)
		elif var_filter == 'category':
			tourneys = Tourney.objects.filter(Console=request.GET.get('console'))

	except ObjectDoesNotExist:
		return render(request, "tourneys/my_tourneys.html", { 'consoles' : ['XBOX ONE', '3DS', 'WII U', 'PLAYSTATION 4'] });

	return render(request, "tourneys/my_tourneys.html", { 'consoles' : ['XBOX ONE', '3DS', 'WII U', 'PLAYSTATION 4'], 'tourneys' : tourneys });

def add_tourney(request):
	try:
		user = User.objects.get(username=request.user)
		date = helpers.getDateFromString( request.POST.get('start_date') )
		tourney = Tourney(Owner=user, Name=request.POST.get('name'), Game=request.POST.get('game'), Max_participants=request.POST.get('max_participants'), Creation_date=datetime.datetime.now() - datetime.timedelta(hours=6), Console=request.POST.get('console'), Start_date=date)
		tourney.save()
	except ObjectDoesNotExist:
		return HttpResponse('User does not exists')

	return HttpResponse( "Success" )

def view_tourney(request, tourney_id):
	try:
		user = User.objects.get(username=request.user)
		tourney = Tourney.objects.get(id=tourney_id)
		is_owner = True if request.user == tourney.Owner else False
		participants = User_Tourney.objects.filter(Id_tourney=tourney_id)
		number_participants = len(participants)
		is_registered = True if len( User_Tourney.objects.filter(Id_tourney=tourney_id, Id_user=user) ) > 0 else False
		full = number_participants == tourney.Max_participants
		today = datetime.datetime.now() - datetime.timedelta(hours=6)
		tourney_date = tourney.Start_date.astimezone(timezone.utc).replace(tzinfo=None)
		has_started = today > tourney_date
		if has_started:
			generateRound1()
	except ObjectDoesNotExist:
		return HttpResponse("Tourney not found")

	return render(request, "tourneys/tourneys.html", { 'tourney' : tourney, 'is_owner' : is_owner, 'registered_count' : number_participants, 'tourney_id' : tourney_id, 'is_registered' : is_registered, 'participants' : participants, 'is_full' :  full, 'has_started' : has_started})

def generateRound1():
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
