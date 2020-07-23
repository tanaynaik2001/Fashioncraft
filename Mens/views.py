from django.shortcuts import render,redirect
from .models import Fashionmen
from django.contrib.auth.models import User,auth
# Create your views here.
def mens(request):
    mens=Fashionmen.objects.all()

    return render(request,'mens.html' ,{'mens':mens})
    
