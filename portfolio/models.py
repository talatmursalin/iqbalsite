from __future__ import unicode_literals

from django.db import models
import os
from django.dispatch import receiver

# Create your models here.

class WeddingImage(models.Model):
    img = models.FileField();
    href = models.CharField(max_length=500)
    caption = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.caption

class JournalImage(models.Model):
    img = models.FileField();
    href = models.CharField(max_length=500)
    caption = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.caption

class PotraitImage(models.Model):
    img = models.FileField();
    href = models.CharField(max_length=500)
    caption = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.caption

class StillImage(models.Model):
    img = models.FileField();
    href = models.CharField(max_length=500)
    caption = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.caption

@receiver(models.signals.pre_save, sender=JournalImage)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = JournalImage.objects.get(pk=instance.pk).img
    except JournalImage.DoesNotExist:
        return False

    print "---------1",old_file.path

    new_file = instance.img
    if not old_file == new_file:
        print "---------2",old_file.path
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
            print "--------3",old_file.path
