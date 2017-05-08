from __future__ import unicode_literals
from django.shortcuts import render
from .models import HomeImage


def index(request):
    all_img  = HomeImage.objects.all()
    return render(request,'home/index.html',{'all_img':all_img})
