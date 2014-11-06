from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from allauth.account.models import EmailAddress

#SETUP

# Create your models here.

#TOURNEY CLASS BEGINS -----------------------------------------------------

class Tourney(models.Model):
    Name = models.CharField(max_length=50)
    Game = models.CharField(max_length=50)
    Start_date = models.DateTimeField('Start Date')
    End_date = models.DateTimeField('End Date')
    Console = models.CharField(max_length=75)
    Winner = models.ForeignKey(User, null=True, blank=True, default = None)

#TORNEY CLASS ENDS ---------------------------------------------------------

#USER PROFILE CLASS BEGINS -------------------------------------------------

class User_Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    country = CountryField(default="MX")

    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            print result
            if len(result):
                return result[0].verified
        return False

User.profile = property(lambda u: User_Profile.objects.get_or_create(user=u)[0])
#USER PROFILE CLASS ENDS ---------------------------------------------------

class Code(models.Model):
	Id_user = models.ForeignKey(User, unique=True)
	FC = models.CharField(max_length=50)
	Console = models.CharField(max_length=75)

class Round(models.Model):
	Id_tourney = models.ForeignKey(Tourney, unique=True)
	Name = models.CharField(max_length=50)
	Start_date = models.DateTimeField('Start Date')
	End_date = models.DateTimeField('End Date')

class Match(models.Model):
	Id_round = models.ForeignKey(Round, unique=True)
	Id_Winner = models.ForeignKey(User, null=True, blank=True, default = None)
	Start_date = models.DateTimeField('Start Date')

class User_Tourney(models.Model):
	Id_tourney = models.ForeignKey(Tourney, unique=True)
	Id_user = models.ForeignKey(User, unique=True)

class User_Match(models.Model):
	Id_match = models.ForeignKey(Match, unique=True)
	Id_user = models.ForeignKey(User, unique=True)
	Arrive_time = models.DateTimeField('Arrive Time')

