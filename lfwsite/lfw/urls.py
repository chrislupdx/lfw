from django.urls import path, include
from . import views


app_name = 'lfw' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
	path('add_entry/', views.add_entry, name='add_entry'),
	path('add_rscl/', views.add_rescl, name='add_rescl'),
	path('display_jobappview/', views.display_jobappview, name='display_jobappview'),
]

#what am I trying to do here?