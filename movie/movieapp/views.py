from django.db.models import F, Sum, Avg, Min, Max, Value
from django.shortcuts import render, get_object_or_404

# Create your views here.
from movieapp.models import Movie


def main_page(request):
    # movies = Movie.objects.order_by(F("year").asc(nulls_last=True), 'rating')
    movies = Movie.objects.annotate(new_budget=F('budget') + 100,
                                    rating_year=F('rating') + F('year'))
    # movies = Movie.objects.filter(rating__gt=80).annotate(new_rating=(F('rating') + 10))
    agg = movies.aggregate(budget=Avg('budget'), rating_max=Max('rating'), rating_min=Min('rating'))
    count_movies = movies.count()
    return render(request, 'movieapp/all_movies.html', {'movies': movies,
                                                        'agg': agg,
                                                        'count_movies': count_movies})


def show_one_movie(request, slug_movie):
    movie = get_object_or_404(Movie, slug=slug_movie)
    d = {'title': movie.name,
         'movie': movie}
    return render(request, 'movieapp/my_movie.html', d)
