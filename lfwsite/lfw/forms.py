from django import forms
from django.forms import ModelForm
from .models import Jobapp

# class Jobappform(forms.Form):
 	# name = models.CharField(max_length=50)
	# description = models.TextField(null=True, blank=True)
	# company = models.CharField(max_length=50, default='No company')
	# user = models.ForeignKey(User, on_delete=models.CASCADE)
	# contact = models.ManyToManyField(Contact, null=True, blank=True)
	# url = models.URLField(null=True, blank=True)
	# resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, null=True, blank=True)
	# coverletter = models.ForeignKey(Resume, on_delete=models.SET_NULL, null=True, blank=True) 
	# followup_touches = models.IntegerField(null=True, blank=True)
	# referred_by = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True)

	# first_contacted = models.DateTimeField(default=datetime.now())
	# last_contacted = models.DateTimeField(default=datetime.now())
	# date_foundbyuser = models.DateTimeField(default=datetime.now())
	# date_due = models.DateTimeField(default=datetime.now())
	# date_applied = models.DateTimeField(default=datetime.now())
	# date_created = models.DateTimeField(default=datetime.now())
	
class Jobappform(ModelForm):
    class Meta:
        # the model to associate with the form
        model = Jobapp
        # a list of all the models' fields you want in the form
        exclude = ['user', 'followup_touches', 'first_contacted', 'last_contacted', 'date_foundbyuser', 'date_due', 'date_applied','date_created']

class Resclform(ModelForm):
	class Meta:
		model = Jobapp
		fields = ('resume', 'coverletter')
