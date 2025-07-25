from django.urls import re_path
from . import views

app_name = 'portfolio'

urlpatterns = [
    re_path(r'^food/$', views.wedding,name='wedding'),
    re_path(r'^travelwild/$', views.potrait,name='potrait'),
    re_path(r'^conceptual/$', views.journal,name='journal'),
    re_path(r'^street/$', views.still,name='still'),
]
