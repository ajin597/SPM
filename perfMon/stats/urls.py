from django.urls import path
from .views import genarateStats

urlpatterns = [
    path('', genarateStats, name='graph'),
]