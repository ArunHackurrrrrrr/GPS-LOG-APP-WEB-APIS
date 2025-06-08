from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class signUp(APIView):
    def post(self, request):
        userData = request.data

        if User.objects.filter(username = userData['user_Mail']).exists():
            return Response({'error':'user already exist','status':'notcreated'})
        else:
            user = User.objects.create_user(
                username = userData['user_Mail'],   
                email = userData['user_Mail'],
                password = userData['user_Password']
            )
            user.save()
            return Response({'error':'', 'status':'created' })



def data(request):
    userData = request.data
    print(userData)
    return Response({'message':'Authenticated!', 'status':'Authorised' })



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def test(request):
    return Response({'message':'Authenticated!', 'status':'Authorised' })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def home(request):
    resposne_to_send = [{'userName':'Arun Gupta'}]
    return Response({'user_name':resposne_to_send})