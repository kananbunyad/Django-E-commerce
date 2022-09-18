from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.api.serializers import RegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import login,authenticate


class LoginAPIView(APIView):

    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        print(username,password,email)
        if not username or not password or not email:
            return Response({"error" : "Plase fill all fields"}, status=status.HTTP_400_BAD_REQUEST)

        check_user = User.objects.filter(username=username).exists()
        if check_user == False:
            return Response({"error": "Username does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username,password=password,email=email)
        
        if user is not None:
            login(request,user)
            token, created = Token.objects.get_or_create(user=request.user)
            data = {
                'token':token.key,
                'user_id':request.user.pk,
                'username': request.user.username
            }
            return Response({"success": "Successfuly login", "data":data}, status=status.HTTP_200_OK)
        else:
            return Response({"error":"Invalid login details"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def registration_view(request):
    
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfuly registered a new user"
            data['email'] = account.email
            data['username'] = account.username
            data['first_name'] = account.first_name
            data["last_name"] = account.last_name
            return Response(serializer.data)
        else:
            return Response(serializer.errors)