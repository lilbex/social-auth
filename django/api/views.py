# views.py
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import FacebookLoginSerializer, GoogleLoginSerializer
from social_django.utils import psa
from .models import User


class HomeView(APIView):
    def get(self, request):
        return Response({"info": "Dispatch rider api"}, status=status.HTTP_200_OK)


class FacebookLogin(APIView):
    def post(self, request):

        @psa()
        def _post_auth(request):
            serializer = FacebookLoginSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                return Response(user.tokens())
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return _post_auth(request)


class GoogleLogin(APIView):
    def post(self, request):

        @psa()
        def _post_auth(request):
            serializer = GoogleLoginSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                return Response(user.tokens())
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return _post_auth(request)


class FacebookRegister(APIView):
    def post(self, request):
        serializer = FacebookLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(user.tokens(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoogleRegister(APIView):
    def post(self, request):
        serializer = GoogleLoginSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data
            email = user.email
            username = email.split('@')[0]
            if not User.objects.filter(email=email).exists():
                user = User.objects.create_user(email=email, username=username)
            return Response(user.tokens(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
