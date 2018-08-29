from django.urls import path, include
from . import views

app_name = 'lfw' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),

]