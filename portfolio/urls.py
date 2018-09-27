from django.conf.urls import url
from . import views

app_name = 'portfolio'

urlpatterns = [
    url(r'^food/$', views.wedding,name='wedding'),
    url(r'^travelwild/$', views.potrait,name='potrait'),
    url(r'^conceptual/$', views.journal,name='journal'),
    url(r'^street/$', views.still,name='still'),
]
