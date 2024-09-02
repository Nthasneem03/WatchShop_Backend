from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', greet),
    path('api/watchList', get_watch, name='Watch_list'),   # get
    path('api/watchCreate', create_watch, name='Watch_create'),  # post
]