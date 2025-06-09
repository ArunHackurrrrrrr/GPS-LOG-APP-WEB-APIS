from rest_framework import serializers
from Dashboard.models import *


class user_details_serialize(serializers.Serializer):
    
    class Meta:
        model = user_Details
        exclude = ['user']