from django.contrib import admin
from .models import WeddingImage,JournalImage,PotraitImage,StillImage

# Register your models here.
admin.site.register(WeddingImage)
admin.site.register(JournalImage)
admin.site.register(PotraitImage)
admin.site.register(StillImage)
