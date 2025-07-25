from django.urls import re_path
from . import views

app_name = 'bio'

urlpatterns = [
    re_path(r'^$', views.bio,name='bio'),
]
