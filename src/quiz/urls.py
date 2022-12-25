from django.urls import path

from .views import quiz, oxtc
urlpatterns = [
  path('lts', quiz, name='ltts'),
  path('oxtc', oxtc, name='oxtc'),
]