from django.contrib import admin
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index),
    path('<int:month>/<int:day>/', views.get_info_by_date),
    path('type/', views.type_horoscope),
    path('type/<str:type_nature>/', views.nature, name='nature'),
    path('<int:int_zodiac>/', views.get_info_about_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope_name'),
]
