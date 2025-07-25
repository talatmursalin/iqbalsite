"""iqbalsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include  # Changed: Replace django.conf.urls.url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Replaced url() with path()
    path('', include('home.urls')),  # Simpler syntax with path()
    path('bio/', include('bio.urls')),
    path('portfolio/', include('portfolio.urls')),
]

handler403 = 'home.views.handler403'  # permission denied
handler404 = 'home.views.handler404'  # page not found
handler400 = 'home.views.handler400'  # bad request
handler500 = 'home.views.handler500'  # server error

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
