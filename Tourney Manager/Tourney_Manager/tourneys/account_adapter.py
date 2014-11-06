from allauth.account.models import EmailAddress

from allauth.exceptions import ImmediateHttpResponse
from allauth.account.adapter import DefaultAccountAdapter
from django.utils.translation import ugettext_lazy as _

from django import forms

class AccountAdapter(DefaultAccountAdapter):

	def clean_email(self, email):

		result = EmailAddress.objects.filter(email=email)
		if len(result):
			raise forms.ValidationError(_("Email already in use"))

		return email
