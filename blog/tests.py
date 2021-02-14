from django.test import TestCase
from django.http import HttpResponse 

def home(request):
	return HttpResponse('<h1>App Home</h1>')



# Create your tests here.
