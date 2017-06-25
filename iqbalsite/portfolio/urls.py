from django.conf.urls import url
from . import views

app_name = 'portfolio'

urlpatterns = [
    url(r'^wedding/$', views.wedding,name='wedding'),
    url(r'^potrait/$', views.potrait,name='potrait'),
    url(r'^journal/$', views.journal,name='journal'),
    url(r'^still/$', views.still,name='still'),
]
