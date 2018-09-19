from django.urls import path, include
from . import views


app_name = 'lfw' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
	path('jobappform/', views.jobappform, name='jobappform'),
	path('add_res/', views.add_res, name='add_res'),
	path('add_cl/', views.add_cl, name='add_cl'),
	path('display_jobappview/', views.display_jobappview, name='display_jobappview'),
	path('display_pipeline/', views.display_pipeline, name='display_pipeline'),
	path('display_canvas/', views.display_canvas, name='display_canvas'),
	path('display_lagging/', views.display_lagging, name='display_lagging'),
	path('lagging_json/', views.lagging_json, name='lagging_json'),
	path('canvas_json/', views.canvas_json, name='canvas_json'),
	path('elapsed_json/', views.elapsed_json, name='elapsed_json'),
	path('display_elapsed/', views.display_elapsed, name='display_elapsed'),
	path('clbuilder/', views.clbuilder, name='clbuilder'),
	path('skills_list/', views.clbuilder, name='skills_list'),
	path('add_skill/', views.skills_input, name='skills_input'),
	path('jobapp_loader/', views.jobapp_loader, name='jobapp_loader'),
	path('cltodo/', views.clbuilder, name='cltodo'),
	path('cllistview/', views.cllistview, name='cllistview'),
	path('jobapplistview/', views.jobapplistview, name='jobapplistview'),
	path('coverletter/edit/<int:pk>/', views.edit_coverletter, name='edit_coverletter'),
	path('edit_jobapp/<int:pk>/', views.edit_jobapp, name='edit_jobapp'),
	path('cllistview/', views.cllistview, name='cllistview'),
	path('jobappstatusupdate/<int:pk>/', views.move_jobapp_status, name='jobappstatusupdate'),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
