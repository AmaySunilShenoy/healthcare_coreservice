from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import path
import os


class LoginView(APIView):
    def post(self, request):
        id = request.data.get('id')
        password = request.data.get('password')
        
        user = authenticate(request, id=id, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

# view for verifying simplejwt and getting user
class VerifyTokenView(APIView):
    def post(self, request):
        token = request.data.get('token')
        try:
            user = RefreshToken(token).user
            return Response({
                'id': user.id,
                'email': user.email
            })
        except:
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)


urlpatterns = [
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/verify/', VerifyTokenView.as_view(), name='verify'),
]
