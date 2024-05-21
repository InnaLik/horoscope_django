from django.contrib import admin
from movieapp.models import Movie
# Register your models here.


admin.site.site_header = 'Наша админка'

admin.site.index_title = 'Фильмы'

class MovieAdmin(admin.ModelAdmin):

    list_display = ['name', 'rating', 'year']


admin.site.register(Movie, MovieAdmin)