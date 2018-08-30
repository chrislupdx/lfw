from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Jobapp(models.Model):
	company = models.TextField(default='nullabledefault')
	jobapp_name = models.TextField(default='nullabledefault')

class Human(models.Model):
	name = models.TextField()