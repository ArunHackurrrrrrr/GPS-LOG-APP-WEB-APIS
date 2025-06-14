from rest_framework import serializers
from Dashboard.models import *


class user_details_serialize(serializers.ModelSerializer):
    
    class Meta:
        model = user_Details
        exclude = ['user','profile_Picture']
        # fields = ['_all_']



class user_Picture_serialize(serializers.ModelSerializer):
    
    class Meta:
        model = images
        fields = ['profile_Picture']

        def user_profile(self, obj):
            request = self.context.get('request')
            profile_url = obj.profile_Picture.url
            return request.build_absolute_uri(profile_url)