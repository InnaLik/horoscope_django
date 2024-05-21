from django.contrib import admin
from movieapp.models import Movie
# Register your models here.


admin.site.site_header = 'Наша админка'

admin.site.index_title = 'Фильмы'
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = ['name', 'rating', 'year']
    list_editable = ['rating', 'year']
    ordering = ['-year', 'name']
    list_per_page = 2


