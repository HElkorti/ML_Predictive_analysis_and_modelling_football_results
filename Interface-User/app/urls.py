from django.urls import path
from .views import *


urlpatterns = [
    path('', predict_page, name='predictPage'),
]