from __future__ import unicode_literals
from django.db import models

class HomeImage(models.Model):
    img = models.FileField();
    href = models.CharField(max_length=500)
    caption = models.CharField(max_length=100)
    backtext = models.TextField(max_length=500)
