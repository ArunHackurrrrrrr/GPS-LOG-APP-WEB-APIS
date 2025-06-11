from Dashboard.utils.serializer import user_details_serialize
from django.contrib.auth.models import User
def get_user_details(user_mail):
    try:
        user = User.objects.get(email = user_mail)
        user_details = user_details_serialize(user.details)
        if user_details.is_valid:
            if user_details=={}:
                print(f'get-user-det-val -> {user_details.data,'--',user_details}')
                return {'message':'no-details'}
            else:
                print(f'12 get user {user_details.data}')
                return user_details.data
        else:
            return user_details.errors
    
    except Exception as e:
        print(e, 'ye hai')
        print(user_details_serialize.errors)
        return {"error":str(e)}