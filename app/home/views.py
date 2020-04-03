
import json

from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound


def home(request):
    context = {}
    return render(request, 'home/home.html', context)
