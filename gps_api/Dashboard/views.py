from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from Dashboard.utils.create_user_detail import create_user_detials
from Dashboard.utils.get_user_details import get_user_details






@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_User_Details(request):
    user = request.user
    user_Data = request.data
    print(user,f'user data .--> {user_Data}')
    try:
        is_added = create_user_detials(user,user_Data)
        print(is_added == True)
        if is_added == True:
            return Response({'message':'detail-allldded'}, status= status.HTTP_201_CREATED)
        else:
            return Response({'message':is_added}, status= status.HTTP_406_NOT_ACCEPTABLE)
    except Exception as e:
        print(e)
        return Response(status= status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_User_Details(request):
    print('in get', request.data)
    user = request.user
    print(f'user {user}')
    try:
        details = get_user_details(user)
        if details['id'] == '':
            print('empty!')
            return Response({'message':'no-details'},status=status.HTTP_200_OK)
        else:
            print('else views 45')
            return Response(details, status= status.HTTP_200_OK)
    except Exception as e:
        print('this is else 45',details)
        print(e,'the except views 46')
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

