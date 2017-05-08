# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import BioImage


def bio(request):
    all_img  = BioImage.objects.all()
    return render(request,'bio/bio.html',{'all_img':all_img})
