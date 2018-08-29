from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class info(models.Model):
	body = models.TextField()
