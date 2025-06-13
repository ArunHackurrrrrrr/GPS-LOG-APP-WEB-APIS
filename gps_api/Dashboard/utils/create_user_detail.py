from Dashboard.utils.serializer import user_details_serialize, user_Picture_serialize
from Dashboard.models import user_Details, images
import datetime

def create_user_detials(User, user_Data):
    try:
        serializer = user_details_serialize(data=user_Data)
        print(f'here serializer {serializer.is_valid()}')
        if serializer.is_valid():
            serializer.save(user=User)  # ✅ pass user
            print(serializer)
            return True 
        print(serializer.errors,'msg')
        for error, messages in serializer.errors.items():
            print(error,'eerrr')
            return error

        # return serializer.errors
    except Exception as e:
        print(e)
        return {"error": str(e)}  # ✅ return string not raw exception

def add_user_profile_picture(User,user_Picture):
    try:

        # images.objects.create(
        #     user = User,
        #     user_profile = user_Picture
        # )
        instance,_= images.objects.get_or_create(user = User)  # YE ,_ KA MATLAB HIA KI PREBOOKING OR BOOKING MATLAB VO INSTANCE OF THE DB EXIST KARE YA NA KARE LAAKE MUGHE DO LAADLE

        serializer = user_Picture_serialize(
            instance=instance,
            data = user_Picture,
            partial = True
        )
        if serializer.is_valid():
            serializer.save()
            print("\nvalid hai dada \n")
            return True
        else:
            print("\nserializer is not \n")
    except Exception as e:
        print("\nthe image err is \n ",e)
        return {"error":str(e)}