from django.contrib import admin

from main.models import Image


# Register your models here.
@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'place', 'create_date')
