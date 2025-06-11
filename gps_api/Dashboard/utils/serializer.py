from rest_framework import serializers
from Dashboard.models import *


class user_details_serialize(serializers.ModelSerializer):
    
    class Meta:
        model = user_Details
        exclude = ['user']
        # fields = ['_all_']