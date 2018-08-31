from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Jobapp
from .forms import Jobappform

def index(request):
	jobapps = Jobapp.objects.all()	
	return render(request,'lfw/index.html', {'jobapps': jobapps})

def display_jobappview(request):
	jobapps = Jobapp.objects.all()
	fields = [f.name for f in Jobapp._meta.get_fields()]
	print(fields)
	return render(request,'lfw/jobappview.html', {'jobapps': jobapps, 'fields':fields})

def add_entry(request):
	
	if request.method == 'POST':
		form = Jobappform(request.POST)
		if form.is_valid():
			jobapp = form.save(commit=False)
			jobapp.user = request.user 
			jobapp.save()
			return redirect(reverse('lfw:index'))
	form = Jobappform()
	context = {'form': form}
	return render(request, 'lfw/jobappform.html', context)
