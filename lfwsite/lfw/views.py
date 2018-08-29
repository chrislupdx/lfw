from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse

def index(request):
    return render(request,'lfw/index.html')