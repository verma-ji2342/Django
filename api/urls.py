"""
urls.py
"""
# pylint: disable-all
from home.views import index, person, edit_person, delete_data, login, testingAPI, PeopleViewSet, RegisterAPI, LoginAPI
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'people', PeopleViewSet, basename='people')
urlpatterns = router.urls




urlpatterns = [
    path('', include(router.urls)),
    path('index/', index),
    path('person/', person),
    path('edit_person/', edit_person),
    path('delete_data/', delete_data),
    path('login/', LoginAPI.as_view()),
    path('testing/', testingAPI.as_view()),
    path('register/', RegisterAPI.as_view())
]