from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def index(request):
	return render(request, 'tourneys/home.html', request)

def profile(request):
	return render(request, 'tourneys/profile.html', request)