from django.urls import path
from Dashboard.views import *
urlpatterns = [
    path('add-user-details/',add_User_Details),
    path('add-user-image/',user_profile_pic),
    path('get-user-details/',get_User_Details),
]
