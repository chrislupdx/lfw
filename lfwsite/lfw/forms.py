from datetime import datetime
from django import forms
from django.template import Template
from material import Layout, Row, Column, Fieldset, Span2, Span3, Span5, Span6, Span10
from django.forms import ModelForm
from .models import Jobapp, Resume, Coverletter, Contact, Skill

class Jobappform(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(required= False)
    company = forms.CharField(max_length=50, required= False)
    contact = forms.ModelChoiceField(queryset=None, required=False)
    url = forms.URLField(max_length=400, required=False)

    coverletter = forms.ModelChoiceField(queryset=None, required=False) 
    resume = forms.ModelChoiceField(queryset=None, required=False) 

    followup_touches = forms.IntegerField(required= False)
    first_contacted = forms.DateTimeField(required= False)
    last_contacted = forms.DateTimeField(required= False)
    date_foundbyuser = forms.DateTimeField(required= False)
    date_due = forms.DateTimeField(required= False)
    date_applied = forms.DateTimeField(required= False)
    date_created = forms.DateTimeField(required= False)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['contact'].queryset = Contact.objects.filter(user=user)
        self.fields['coverletter'].queryset = Coverletter.objects.filter(user=user)
        self.fields['resume'].queryset = Resume.objects.filter(user=user)
    
    layout = Layout('name', 'company', 'description',
                Row('contact', 'coverletter', 'resume', 'url'),
                Row('followup_touches', 'first_contacted', 'last_contacted'),
                Row('date_foundbyuser', 'date_due', 'date_applied', 'date_created'))


# class Jobappform(ModelForm):
#     class Meta:
#         # the model to associate with the form
#         model = Jobapp
#         # a list of all the models' fields you want in the form
#         exclude = ['user', 'followup_touches', 'first_contacted', 'last_contacted', 'date_due', 'date_applied','date_created']
#         widgets = {
#                  'resume': Select(lookups=['name__icontains']),
#                  'coverletter': Select(lookups=['name__icontains'])
#              }

#     layout = Layout(
#         Row('name'),
#         Row('company', 'referred_by'),
#         Row('description', 'url'),
#         Row('date_rolecreated'),
#         Row('coverletter', 'resume'))   

class Resumeform(ModelForm):
    class Meta:
        model = Resume
        fields = ('url', 'name',)

class Clform(ModelForm):
    class Meta:
        model = Coverletter
        fields = ('url', 'name',)

class Skills_input(ModelForm):
    class Meta:
        model = Skill
        fields = ('name', 'copy',)