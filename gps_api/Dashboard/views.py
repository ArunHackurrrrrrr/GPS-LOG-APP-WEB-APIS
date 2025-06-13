from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from Dashboard.utils.create_user_detail import create_user_detials , add_user_profile_picture
from Dashboard.utils.get_user_details import get_user_details
from Dashboard.models import user_Details






@api_view(['POST'])
@permission_classes([IsAuthenticated])
# @parser_classes([MultiPartParser, FormParser])
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
    # print('in get', request.data)
    user = request.user
    # print(f'user {user}')
    try:
        details = get_user_details(user)
        if not details.get('id'):
            print('empty!')
            return Response({'message':'no-details'},status=status.HTTP_200_OK)
        else:
            # print('else views 45')
            return Response(details, status= status.HTTP_200_OK)
    except Exception as e:
        # print('this is else 45',details)
        print(e,'the except views 46')
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

