from django.contrib import admin

from core.models import Film

admin.site.register(Film)


class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'group')
