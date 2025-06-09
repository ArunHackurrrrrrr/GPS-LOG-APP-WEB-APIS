from Dashboard.utils.serializer import user_details_serialize
from django.contrib.auth.models import User
def get_user_details(user_mail):
    try:
        user = User.objects.get(email = user_mail)
        user_details = user_details_serialize(user.details)
        if user_details.is_valid:
            return user_details.data
        else :
            return user_details.error_messages
    
    except Exception as e:
        return False