from django.db import models
from datetime import datetime, timedelta, timezone
from django.contrib.auth.models import User

class Company(models.Model):
	name = models.CharField(max_length=25)
	description = models.TextField(null=True, blank=True)
	IPO = models.BooleanField()
	Solo = range(0, 6)
	Tiny = range(6,26)
	Little = range(26,51)
	Small = range(51 ,101)
	Smallish = range(101 ,251)
	Medium = range(251 ,401)
	Largish = range(401 ,601)
	Corporate_entity = range(601 ,5000)

	COMPANY_SIZE_CHOICES = (
		('SL', 'SOLO'),
		('TN', 'TINY'),
		('LT', 'LITTLE'),
		('SM', 'SMALL'),
		('SM', 'SMALLISH'),
		('MD', 'MEDIUM'),
		('LG', 'LARGEISH'),
		('CE', 'CORPORATE_ENTITY'),
		)
	company_size = models.CharField(
		max_length=2,
		choices=COMPANY_SIZE_CHOICES,
		default= Tiny,
		)

	def startup_sized(self):
		return self.app_contact_status in (self.TINY, self.LITTLE, self.SMALL, self.SMALLISH, self.MEDIUM)


class Contact(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=25, null=True, blank=True)
	last_name = models.CharField(max_length=25, null=True, blank=True)
	company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
	email = models.EmailField(max_length=70, null=True, blank=True)
	linkedin = models.URLField(null=True, blank=True)
	facebook = models.URLField(null=True, blank=True)
	instagram = models.URLField(null=True, blank=True)
	twitter = models.URLField(null=True, blank=True)
	years_at_company = models.IntegerField(null=True, blank=True)
	title = models.CharField(max_length=50)
	
	date_met = models.DateTimeField(blank=True, null=True)
	last_soft_communication = models.DateTimeField(blank=True, null=True)
	last_contacted = models.DateTimeField(blank=True, null=True)
	first_contacted = models.DateTimeField(blank=True, null=True)

	first_contacted = models.DateTimeField(default=datetime.now())
	last_contacted = models.DateTimeField(default=datetime.now())
	date_rolecreated = models.DateTimeField(blank=True, null=True)
	date_due = models.DateTimeField(default=datetime.now())
	date_applied = models.DateTimeField(default=datetime.now())
	date_created = models.DateTimeField(default=datetime.now())


	UNDEFINED = 5
	SOCIAL = 10
	ANCILLARY = 50
	Job_REFERRAL = 80
	HIRING_MANAGER = 'MG'
	PIPELINE_STATUS_CHOICES = (
		('UD', 'UNDEFINED'),
		('SC', 'Social'),
		('AC', 'Ancillary'),
		('RF', 'Job_Referral'),
		('MG', 'Hiring Manager'),
		)
	app_contact_status = models.CharField(
		max_length=2,
		choices=PIPELINE_STATUS_CHOICES,
		default=UNDEFINED,
		)
	def is_app_related(self):
		return self.app_contact_status in (self.HIRING_MANAGER, self.JOB_REFERRAL)

class Resume(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	url = models.URLField(null=True, blank=True)
	date_created = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return str(self.name)

class Coverletter(models.Model):
	
	name = models.CharField(max_length=50, blank=True, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	url = models.URLField(null=True, blank=True)
	clcopy = models.TextField()

class Jobapp(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(null=True, blank=True)
	company = models.CharField(max_length=50, default='No company')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	followup_touches = models.IntegerField(null=True, blank=True)
	contact = models.ManyToManyField(Contact, blank=True)
	url = models.URLField(null=True, blank=True)
	resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, null=True, blank=True)
	coverletter = models.ForeignKey(Coverletter, on_delete=models.SET_NULL, null=True, blank=True) 
	referred_by = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True, related_name='referred_by')

	first_contacted = models.DateTimeField(blank=True, null=True)
	last_contacted = models.DateTimeField(blank=True, null=True)
	date_rolecreated = models.DateTimeField(blank=True, null=True)
	date_due = models.DateTimeField(blank=True, null=True)
	date_applied = models.DateTimeField(blank=True, null=True)
	date_created = models.DateTimeField(default=datetime.now())


	JOBAPP_STATS_CHOICES = (
		('PS', 'PROSPECT'),
		('RO', 'REACHEDOUT'),
		('QD', 'QUALIFIED'),
		('SN', 'SCREENING'),
		)
	pipeline_status = models.CharField(
		max_length=2,
		choices=JOBAPP_STATS_CHOICES,
		default='PS',
		)

	@property	
	def time_elapsed(self):
		now = datetime.now(timezone.utc)
		elapsed = now - self.date_created
		return elapsed	
	
class Skill(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	copy = models.TextField()
	coverletter = models.ManyToManyField(Coverletter, blank=True, related_name='skills')

	def __str__(self):
		return str(self.name)