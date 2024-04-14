from django.urls import path, register_converter
from . import views, convertors

register_converter(convertors.FourDigitConverter, 'yyyy')
register_converter(convertors.MyFloatConverter, 'my_float')

urlpatterns = [
    path('', views.main_menu, name='main'),
    path('type/', views.main_type),
    path('type/<str:element>/', views.type_zodiac, name='type_zodiac'),
    path('people/', views.people, name='people_all'),
    # path('<yyyy:zodiak>/', views.get_converters),
    # path('<my_float:zodiak>/', views.float_converters),
    # path('<int:zodiak>/', views.by_number, name='horoscope_int'),
    path('<str:zodiak>/', views.zod, name='horoscope_name'),
    # path('<int:month>/<int:day>/', views.horoscope_month)
]
