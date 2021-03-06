from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Jobapp, Resume, Coverletter, Skill, Coverlettertemplate
from .forms import Jobappform, Resumeform, Clform, Skills_input, CoverletterForm
from django.contrib.auth.decorators import permission_required, login_required
from django import forms

@login_required()
def index(request):
	return render(request,'lfw/index.html', status_context(request))

def display_jobappview(request):
	jobapps = Jobapp.objects.filter(user=request.user)
	fields = [f.name for f in Jobapp._meta.get_fields()]
	print(fields)
	return render(request,'lfw/jobappview.html', {'jobapps': jobapps, 'fields':fields})

def display_elapsed(request):
	pipeline_individual_count = Jobapp.objects.filter(user=request.user)
	return render(request,'lfw/display_elapsed.html', status_context(request))

def display_lagging(request):
	pipeline_individual_count = Jobapp.objects.filter(user=request.user)
	return render(request,'lfw/display_lagging.html', status_context(request))

def lagging_json(request):
	jobapps = serializers.serialize("json", Jobapp.objects.filter(user=request.user, pipeline_status='PS'))
	return JsonResponse(jobapps, safe=False) #this return could be redundant, who knows

def elapsed_json(request):
	first_group = [app for app in Jobapp.objects.filter(user=request.user) if 0 <= app.time_elapsed.days < 5]
	second_group = [app for app in Jobapp.objects.filter(user=request.user) if 5 < app.time_elapsed.days < 10]
	third_group = [app for app in Jobapp.objects.filter(user=request.user) if 10 < app.time_elapsed.days < 15]
	fourth_group = [app for app in Jobapp.objects.filter(user=request.user) if 15 < app.time_elapsed.days < 20]
	fifth_group = [app for app in Jobapp.objects.filter(user=request.user) if 20 < app.time_elapsed.days < 25]
	sixth_group = [app for app in Jobapp.objects.filter(user=request.user) if 25 < app.time_elapsed.days < 30]
	data = [len(first_group), len(second_group), len(third_group), len(fourth_group), len(fifth_group), len(sixth_group)]
	return JsonResponse(data, safe=False)

def canvas_json(request):
	jobapps = serializers.serialize("json", Jobapp.objects.filter(user=request.user), fields=('pipeline_status'))
	return JsonResponse(jobapps, safe=False) #this return could be redundant, who knows

def display_canvas(request):
	pipeline_individual_count = Jobapp.objects.filter(user=request.user)
	return render(request,'lfw/canvas.html', status_context(request))

def display_pipeline(request):
	return render(request,'lfw/pipeline.html', status_context(request))

def jobappform(request):
	if request.method == 'POST':
		form = Jobappform(user=request.user)
		app = Jobapp()
		for k, v in request.POST.items():
			print('label: {}'.format(k))
			print('value: {}'.format(v))
		app.name = request.POST.get('name')
		app.user = request.user
		app.company = request.POST.get('company')
		app.description = request.POST.get('description')
		app.url = request. POST.get('url')
		app.date_rolecreated = request.POST.get('date_rolecreated')
		print(request.POST.get('resume'))
		if request.POST.get('resume'):
			app.resume = Resume.objects.get(pk=request.POST.get('resume'))
		if request.POST.get('coverletter'): 
			app.coverletter = Coverletter.objects.get(pk=request.POST.get('coverletter'))
		app.save()
		# if form.is_valid():
		# 	print('addentry is valdi')
		# 	jobapp = form.save(commit=False)
		# 	jobapp.exuser = request.user 
		# 	jobapp.save()
		return redirect(reverse('lfw:index'))
	form = Jobappform(request.user)
	print(form)
	context = {'form': form}
	return render(request, 'lfw/jobappform.html', context)

def skills_input(request):
	if request.method == 'POST':
		form = Skills_input(request.POST)
		if form.is_valid():
			cl = form.save(commit=False)
			cl.user = request.user
			cl.save()
	form = Skills_input()
	context = {'form': form}
	return render(request, 'lfw/skills_input.html', context)	 

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

def clbuilder(request):
	if request.method == 'POST':
		form = CoverletterForm(request.user)
		coverletter = Coverletter()
		coverletter.user = request.user
		coverletter.clcopy = request.POST.get('coverlettercopy')
		coverletter.save()
		
		skills = request.POST.getlist('skills')
		for skillID in skills:
			skill = get_object_or_404(Skill, pk=skillID)
			coverletter.skills.add(skill)
		coverletter.save()
		
		jobappID = request.POST.get('jobapp')
		if jobappID and jobappID != "none":
			jobappID = int(jobappID)
			jobapp = get_object_or_404(Jobapp, pk=jobappID)
			jobapp.coverletter = coverletter
			jobapp.save()

	form = CoverletterForm(request.user)	

	coverlettertemplates = Coverlettertemplate.objects.filter(user=request.user)
	jobapps = Jobapp.objects.filter(user=request.user)
	skills = Skill.objects.filter(user=request.user)

	context = {
	'skills':skills,
	'jobapps':jobapps,
	'form': form,
	'coverlettertemplates' :coverlettertemplates,
	}
	return render(request, 'lfw/clbuilder.html', context)

def status_context(request):
	jobapps = Jobapp.objects.filter(user=request.user)
	prospects = jobapps.filter(pipeline_status='PS')
	reachedout = jobapps.filter(pipeline_status='RO')
	qualified = jobapps.filter(pipeline_status='QD')
	screening = jobapps.filter(pipeline_status='SN')
	context = {
		'jobapps': jobapps,
		'prospects' : prospects,
		'reachedout' : reachedout,
		'qualified' : qualified,
		'screening' : screening,
	}
	return context	

def jobapp_loader(request):
	jobapps = serializers.serialize("json", Jobapp.objects.filter(user=request.user))
	return JsonResponse(jobapps, safe=False)

def coverlettertemplate_loader(request):
	coverlettertemplates = serializers.serialize("json", Coverlettertemplate.objects.filter(user=request.user))
	return JsonResponse(coverlettertemplates, safe=False)

def cllistview(request):
	coverletter = Coverletter.objects.filter(user=request.user)
	context = {'coverletter' :coverletter,}
	return render(request, 'lfw/cllistview.html', context)
 
def jobapplistview(request):
	jobapp = Jobapp.objects.filter(user=request.user)
	context = {'jobapp' :jobapp,}
	return render(request, 'lfw/jobapplistview.html', context)

def edit_coverletter(request, pk):
	coverletter = get_object_or_404(Coverletter, pk=pk)

	if request.method == 'POST':
		form = CoverletterForm(request.user)
		coverletter.clcopy = request.POST.get('coverlettercopy')
		coverletter.save()
		
		skills = request.POST.getlist('skills')
		for skillID in skills:
			skill = get_object_or_404(Skill, pk=skillID)
			coverletter.skills.add(skill)
		coverletter.save()

		jobappID = request.POST.get('jobapp')
		if jobappID and jobappID != "none":
			jobappID = int(jobappID)
			jobapp = get_object_or_404(Jobapp, pk=jobappID)
			jobapp.coverletter = coverletter
			jobapp.save()

		return redirect('lfw:edit_coverletter', pk=pk)

	jobapps = Jobapp.objects.filter(user=request.user)
	form = CoverletterForm(request.user, initial={ 'coverlettercopy':coverletter.clcopy})
	return render(request, 'lfw/cleditor.html', {
		'form': form,
		'jobapps':jobapps,
		'pk': pk
	})

def edit_jobapp(request, pk):
	app = get_object_or_404(Jobapp, pk=pk)

	if request.method == 'POST':
		form = Jobappform(user=request.user)
		for k, v in request.POST.items():
			print('label: {}'.format(k))
			print('value: {}'.format(v))
		app.name = request.POST.get('name')
		app.user = request.user
		app.company = request.POST.get('company')
		app.description = request.POST.get('description')
		app.url = request. POST.get('url')
		app.date_rolecreated = request.POST.get('date_rolecreated')
		print(request.POST.get('resume'))
		if request.POST.get('resume'):
			app.resume = Resume.objects.get(pk=request.POST.get('resume'))
		if request.POST.get('coverletter'): 
			app.coverletter = Coverletter.objects.get(pk=request.POST.get('coverletter'))
		app.save()
		# if form.is_valid():
		# 	print('addentry is valdi')
		# 	jobapp = form.save(commit=False)
		# 	jobapp.exuser = request.user 
		# 	jobapp.save()
		return redirect(reverse('lfw:index'))

		return redirect('lfw:edit_jobapp', pk=pk)

	existing_app = {
		'name': app.name,
		'company': app.company,
		'description': app.description,
		'url': app.url,
		'date_rolecreated': app.date_rolecreated,
		'resume': app.resume,
		'coverletter': app.coverletter
	}
	form = Jobappform(request.user, initial=existing_app)
	return render(request, 'lfw/jobappeditor.html', {
		'form': form,
		'pk': pk
	})

def move_jobapp_status(request, pk):
	app = get_object_or_404(Jobapp, pk=pk)

	if app.pipeline_status == 'PS':
		app.pipeline_status = 'RO'
	
	elif app.pipeline_status == 'RO':
		app.pipeline_status = 'QD'
	
	elif app.pipeline_status == 'QD':
		app.pipeline_status = 'SN'
	app.save()
	return redirect('lfw:index')

def coverlettertemplateselect(request):
	coverletter = Coverletter.objects.filter(user=request.user)
	context = {'coverletter' : coverletter,}
	return request


# @login_required
# def index_view(request):
#    p = Model.objects.filter(user=request.user)
#    return render(request, 'app/index.html', {'objects': p})

# def all_forms(request):
# 	context = {}

# 	if request.method == 'POST':
# 		entry_form = Jobappform(request.POST)
# 		if entry_form.is_valid():
# 			jobapp = entry_form.save(commit=False)
# 			jobapp.user = request.user 
# 			jobapp.save()
# 	entry_form = Jobappform()
# 	context['add_entry_form'] = entry_form

# 	if request.method == 'POST':
# 		res_form = Resumeform(request.POST)
# 		if res_form.is_valid():
# 			resume = res_form.save(commit=False)
# 			resume.user = request.user
# 			resume.save()
# 	res_form = Resumeform()
# 	context['resume_form'] = res_form

# 	if request.method == 'POST':
# 		cl_form = Clform(request.POST)
# 		if cl_form.is_valid():
# 			cl = form.save(commit=False)
# 			cl.user = request.user
# 			cl.save()
# 	cl_form = Clform()
# 	context['coverletter_form'] = cl_form

# 	return render(request, 'lfw/all_forms.html', context)