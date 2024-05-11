from django.urls import path, include

from blog import views

urlpatterns = [
    path('', views.start),
    path('posts/', views.posts),
    path('beautiful_table/', views.bea_table)
]
