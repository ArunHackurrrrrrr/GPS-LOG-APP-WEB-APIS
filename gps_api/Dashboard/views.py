from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from Dashboard.utils.create_user_detail import create_user_detials , add_user_profile_picture
from Dashboard.utils.get_user_details import get_user_details
from Dashboard.models import images
from Dashboard.utils.serializer import user_Picture_serialize






@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_User_Details(request):
    print(request.data)
    user = request.user
    user_Data = request.data
    # print(user,f'user data .--> {user_Data}')
    try:
        is_added = create_user_detials(user,user_Data)
        # print(is_added == True)
        if is_added == True:
            return Response({'message':'detail-added'}, status= status.HTTP_200_OK)
        else:
            # print('else 30 add details view \n',type(is_added))
            return Response({'message':is_added}, status= status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status= status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def user_profile_pic(request):
    data = request.data
    user = request.user
    print("\n \n !!!!INSIDE THE IMAGE \n \n")
    try:
        print('inside the try')
        is_added = add_user_profile_picture(user,data)
        if is_added == True:
            return Response({'message':'detail-added'}, status= status.HTTP_200_OK)
        else:
            print('\nelse 28\n',type(is_added))
            return Response({'message':is_added}, status= status.HTTP_200_OK)
    
    except Exception as e:
        print(e,'in view img \n')
        return Response(status= status.HTTP_500_INTERNAL_SERVER_ERROR)






    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_User_Details(request):
    user = request.user
    try:

        details = get_user_details(user,request)
        if not details.get('id'):
            print('empty!')
            return Response({'message':'no-details'},status=status.HTTP_200_OK)
        else:
            user_profile = images.objects.get(user = user)
            serializer = user_Picture_serialize(user_profile, context={"request": request})
            print('else views 77') # DATA IS GOING PERFECTLY USING BELOW , WE'VE TO MODIFY SOME DATA CLASS IN ANDROID APP
            combined_data = {**details,**serializer.data}
            print(combined_data)
            return Response(combined_data, status= status.HTTP_200_OK)
    except Exception as e:
        # print('this is else 45',details)
        print(e,'the except views 46')
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR) #FIX IT OTHER WISE IT'LL GIVE YOU SERVER ERROR CAUSE INFINITE LOADING OR APP CRASH
    

