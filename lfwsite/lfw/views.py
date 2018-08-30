from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Jobapp

def index(request):
	jobapp = Jobapp.objects.all()	
	return render(request,'lfw/index.html')

def add_entry(request):
	
	if request.method == 'POST':
		Jobappname = request.POST['JobappName']
		Companyname = request.POST['CompanyName'] 
		Jobapp_entry = Jobapp(jobapp_name = Jobappname, company = Companyname)
		Jobapp_entry.save()
	return redirect(reverse('lfw:index'))