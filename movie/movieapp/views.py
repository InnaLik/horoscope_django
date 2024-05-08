from django.db.models import F
from django.shortcuts import render, get_object_or_404

# Create your views here.
from movieapp.models import Movie


def main_page(request):
    movies = Movie.objects.order_by(F("year").asc(nulls_last=True), 'rating')
    return render(request, 'movieapp/all_movies.html', {'movies': movies})


def show_one_movie(request, slug_movie):
    movie = get_object_or_404(Movie, slug=slug_movie)
    d = {'title': movie.name,
         'movie': movie}
    return render(request, 'movieapp/my_movie.html', d)
