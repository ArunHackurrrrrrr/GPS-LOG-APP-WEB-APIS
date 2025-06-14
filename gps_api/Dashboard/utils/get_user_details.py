from Dashboard.utils.serializer import user_details_serialize,user_Picture_serialize
from django.contrib.auth.models import User
from Dashboard.models import images
def get_user_details(user_mail,request):
    try:
        user = User.objects.get(email = user_mail)
        user_details = user_details_serialize(user.details)
        if user_details.is_valid:
            if user_details=={}:
                return {'message':'no-details'}
            else:
                return user_details.data
        else:
            return user_details.errors
    
    except Exception as e:
        print(e, 'ye hai get ka \n')
        print(user_details_serialize.errors)
        return {"error":str(e)}