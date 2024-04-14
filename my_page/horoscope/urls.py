from django.urls import path, register_converter
from . import views, convertors

register_converter(convertors.FourDigitConverter, 'yyyy')
register_converter(convertors.MyFloatConverter, 'my_float')

urlpatterns = [
    path('', views.main_menu, name='main'),
    path('<str:zodiak>/', views.zod, name='horoscope_name'),
]
