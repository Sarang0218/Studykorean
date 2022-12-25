from django.urls import path
from .views import home, signupview,maintab, loginview, quiz, correct, incorrect
urlpatterns = [
  path('', home, name="home"),
  path('signup/', signupview, name="signup"),
  path('home/', maintab, name="tabs"),
  path('login/', loginview, name="login"),
  path('incorrect/', incorrect, name="incorrect"),
  path('correct/', correct, name="correct"),
  path('quiz/', quiz, name="quiz"),
  
]