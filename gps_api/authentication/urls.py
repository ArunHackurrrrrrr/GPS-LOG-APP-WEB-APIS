from django.urls import path, include
from authentication.views import *
urlpatterns = [
    path('login/',test),
    path('signUp',signUp.as_view()),
    path('home',home)
]
