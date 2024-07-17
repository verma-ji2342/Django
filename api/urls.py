"""
urls.py
"""
# pylint: disable-all
from home.views import index, person, edit_person, delete_data, login, testingAPI
from django.urls import path




urlpatterns = [
    path('index/', index),
    path('person/', person),
    path('edit_person/', edit_person),
    path('delete_data/', delete_data),
    path('login/', login),
    path('testing/', testingAPI.as_view())
]