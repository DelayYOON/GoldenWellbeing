
from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.
from .models import Lecture

admin.site.register(Lecture)


@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):

    """ """
    """ Phot Admin Definition """

    pass
    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
