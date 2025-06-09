from django.urls import path, include
from Dashboard.views import *
urlpatterns = [
    path('add-user-details/',add_User_Details),
    path('get-user-details/',get_User_Details)
]
