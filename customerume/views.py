from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from ume.forms import ServiceProviderPost
from accounts.models import CustomUser
from ume.models import sellerPost
from accounts.urls import *
# Create your views here.

def index(request):
    return render(request,'ume/home.html')