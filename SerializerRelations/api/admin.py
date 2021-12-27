from django.contrib import admin
from .models import Songs, Singer


@admin.register(Songs)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'singer', 'duration']


@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender']
