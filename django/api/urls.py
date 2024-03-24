from django.urls import path

from .views import (
HomeView,
FacebookLogin,
GoogleLogin,
FacebookRegister,
GoogleRegister
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/facebook/', FacebookRegister.as_view(), name='fb_register'),
    path('register/google/', GoogleRegister.as_view(), name='google_register'),
    path('login/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('login/google/', GoogleLogin.as_view(), name='google_login'),
]
