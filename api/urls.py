"""
urls.py
"""
# pylint: disable-all
from home.views import index, person, edit_person 
from django.urls import path




urlpatterns = [
    path('index/', index),
    path('person/', person),
    path('edit_person/', edit_person)
]