from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from social_core.exceptions import MissingBackend, AuthFailed
from social_django.utils import load_backend, load_strategy
from .models import User


class FacebookLoginSerializer(serializers.Serializer):
    access_token = serializers.CharField()

    def validate_access_token(self, access_token):
        backend = 'facebook'
        strategy = load_strategy(request=None)
        try:
            backend = load_backend(strategy, backend, reverse=True)
        except MissingBackend:
            raise serializers.ValidationError('Invalid authentication backend')

        try:
            user = backend.do_auth(access_token)
        except AuthFailed as e:
            raise AuthenticationFailed(f'Invalid access token {str(e)}')

        if not user:
            raise AuthenticationFailed('Invalid access token')

        return user

    def create(self, validated_data):
        user = validated_data
        email = user['email']
        username = email.split('@')[0]  # Extracting username from email
        if not User.objects.filter(email=email).exists():
            user = User.objects.create_user(email=email, username=username)
        return user
    
class GoogleLoginSerializer(serializers.Serializer):
    access_token = serializers.CharField()

    def validate_access_token(self, access_token):
        if not access_token:
            raise serializers.ValidationError('Access token is required')

        backend_name = 'google-oauth2'
        redirect_uri = 'google.com'  # Provide the appropriate redirect URI for your application
        strategy = load_strategy()
        try:
            backend = load_backend(strategy, backend_name, redirect_uri=redirect_uri)
        except MissingBackend:
            raise serializers.ValidationError('Invalid authentication backend')

        try:
            user = backend.do_auth(access_token)
        except AuthFailed as e:
            raise AuthenticationFailed(f'Invalid access token: {str(e)}')

        if not user or user.is_anonymous:
            raise AuthenticationFailed('Invalid access token')

        return user

