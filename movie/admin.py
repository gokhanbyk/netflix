from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'show_genre', 'view_count')

    def show_genre(self, obj):
        liste = '<ul>'
        for i in obj.genre.all():
            liste += f'<li>{i}</li>'
        liste += '</ul>'
        return mark_safe(liste)



admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movies, MovieAdmin)