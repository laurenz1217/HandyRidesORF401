from django.urls import path
from . import views

app_name = "rides"

urlpatterns = [
    path('', views.index, name='index'),
    path('rides/', views.rides, name='rides'),
    path('search/', views.ride_search, name='ride_search'),
    path('create/', views.create, name='create')
]
