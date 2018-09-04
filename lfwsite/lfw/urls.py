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
]

#what am I trying to do here?