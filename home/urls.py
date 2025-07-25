from django.urls import path  # Replaced django.conf.urls.url
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),  # Replaced url() with path()
]