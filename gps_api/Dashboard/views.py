from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from utils.create_user_detail import create_user_detials

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_User_Details(request):
    user = request.user
    user_Data = request.data
    try:{
        create_user_detials(user,user_Data)
    }
    except Exception as e:{
        print(e)
    }
    return Response()
    
