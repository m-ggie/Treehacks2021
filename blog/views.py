from django.shortcuts import render
from django.test import TestCase
from .models import question



def home(request):
	context = {
		'question': question.objects.all()
	}
	return render(request, 'blog/home.html',  context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})	

def survey(request):
	context = {
		'question': question.objects.all()
	}
	return render(request, 'blog/survey.html',  context)


# Create your views here.
