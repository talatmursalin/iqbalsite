from __future__ import unicode_literals
from django.shortcuts import render
from .models import HomeImage


def index(request):
    all_img = HomeImage.objects.all()
    return render(request, 'home/index.html', {'all_img': all_img})


def handler403(request, exception):
    return render(request, 'home/403.html', status=403)


def handler404(request, exception):
    return render(request, 'home/404.html', status=404)


def handler400(request, exception):
    return render(request, 'home/400.html', status=400)


def handler500(request):
    return render(request, 'home/500.html', status=500)
