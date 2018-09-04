from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Jobapp, Resume, Coverletter
from .forms import Jobappform, Resumeform, Clform

def index(request):
	return render(request,'lfw/index.html', status_context())

def display_jobappview(request):
	jobapps = Jobapp.objects.all()
	fields = [f.name for f in Jobapp._meta.get_fields()]
	print(fields)
	return render(request,'lfw/jobappview.html', {'jobapps': jobapps, 'fields':fields})

def display_pipeline(request):

	return render(request,'lfw/pipeline.html', status_context())

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

def add_res(request):
	if request.method == 'POST':
		form = Resumeform(request.POST)
		if form.is_valid():
			resume = form.save(commit=False)
			resume.user = request.user
			resume.save()
			
			return redirect(reverse('lfw:index'))
	form = Resumeform()
	context = {'form': form}
	return render(request, 'lfw/Res_form.html', context)

#is this a context that's getting passed bewteen the front to middle or middle to back?

def add_cl(request):
	if request.method == 'POST':
		form = Clform(request.POST)
		if form.is_valid():
			cl = form.save(commit=False)
			cl.user = request.user
			cl.save()
			return redirect(reverse('lfw:index'))
	form = Clform()
	context = {'form': form}
	return render(request, 'lfw/cl_form.html', context)
#is this a context that's getting passed bewteen the front to middle or middle to back?


def status_context():
	jobapps = Jobapp.objects.all()
	prospects = Jobapp.objects.filter(pipeline_status='PS')
	reachedout = Jobapp.objects.filter(pipeline_status='RO')
	qualified = Jobapp.objects.filter(pipeline_status='QD')
	screening = Jobapp.objects.filter(pipeline_status='SN')
	context = {
		'jobapps': jobapps,
		'prospects' : prospects,
		'reachedout' : reachedout,
		'qualified' : qualified,
		'screening' : screening,
	}
	return context	