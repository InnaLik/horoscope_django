from django.urls import path
from . import views

urlpatterns = [
    path('<int:zodiak>/', views.by_number, name='horoscope_int'),
    path('<str:zodiak>/', views.zod, name='horoscope_name')
]
