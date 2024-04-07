from django.urls import path
from . import views

urlpatterns = [
    path('<int:zodiak>/', views.by_number),
    path('<str:zodiak>/', views.zod)
]
