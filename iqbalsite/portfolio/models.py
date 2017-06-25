from __future__ import unicode_literals

from django.db import models

# Create your models here.

class WeddingImage(models.Model):
    img = models.FileField();
    href = models.CharField(max_length=500)
    caption = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)

class JournalImage(models.Model):
    img = models.FileField();
    href = models.CharField(max_length=500)
    caption = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)

class PotraitImage(models.Model):
    img = models.FileField();
    href = models.CharField(max_length=500)
    caption = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)

class StillImage(models.Model):
    img = models.FileField();
    href = models.CharField(max_length=500)
    caption = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
