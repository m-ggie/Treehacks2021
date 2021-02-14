from django.db import models
from django.contrib.auth.models import User

class question(models.Model):
	q = models.CharField(max_length = 100)
	answer1 = models.CharField(max_length = 100)
	answer2 = models.CharField(max_length = 100)
	answer3 = models.CharField(max_length = 100)
	answer4 = models.CharField(max_length = 100)
	answer5 = models.CharField(max_length = 100)
	answer6 = models.CharField(max_length = 100)
	answer7 = models.CharField(max_length = 100)
	answer8 =  models.CharField(max_length = 100)
	answer9 = models.CharField(max_length = 100)
	answer10 = models.CharField(max_length = 100)
	answer11 = models.CharField(max_length = 100)
	answer12 = models.CharField(max_length = 100)
	qtype = models.CharField(max_length = 100)



 



 