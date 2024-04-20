from django.urls import path

from movieapp import views

urlpatterns = [
    path('', views.main_page, name='home'),
    path('<slug:slug_movie>/', views.shoe_one_movie, name='one_movie'),
]
