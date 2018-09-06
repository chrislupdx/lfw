from django.urls import path, include
from . import views


app_name = 'lfw' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
	path('add_entry/', views.add_entry, name='add_entry'),
	path('add_res/', views.add_res, name='add_res'),
	path('add_cl/', views.add_cl, name='add_cl'),
	path('display_jobappview/', views.display_jobappview, name='display_jobappview'),
	path('display_pipeline/', views.display_pipeline, name='display_pipeline'),
	path('display_canvas/', views.display_canvas, name='display_canvas'),
	path('canvas_json/', views.canvas_json, name='canvas_json'),
	path('elapsed_json/', views.elapsed_json, name='elapsed_json'),
	path('display_elapsed/', views.display_elapsed, name='display_elapsed'),
]

#what am I trying to do here?