from django.shortcuts import render
from django.http import HttpResponse
from .models import JournalImage, PotraitImage, StillImage, WeddingImage


# Create your views here.
def wedding(request):
    context = {}
    return render(request, 'portfolio/wedding.html', context)


def journal(request):
    all_img = reversed(JournalImage.objects.all())
    x = 0
    temp = list()
    data = list()
    for al in all_img:
        temp.append(al)
        x += 1
        if x % 3 == 0:
            data.append(temp)
            temp = list()
    return render(request, 'portfolio/journal.html', {'data': data})


def potrait(request):
    all_img = PotraitImage.objects.all()
    x = 0
    temp = list()
    data = list()
    for al in all_img:
        temp.append(al)
        x += 1
        if x % 3 == 0:
            data.append(temp)
            temp = list()
    return render(request, 'portfolio/potrait.html', {'data': data})


def still(request):
    all_img = StillImage.objects.all()
    x = 0
    temp = list()
    data = list()
    for al in all_img:
        temp.append(al)
        x += 1
        if x % 3 == 0:
            data.append(temp)
            temp = list()
    return render(request, 'portfolio/still.html', {'data': data})
