from django.urls import path
from django.contrib.auth.views import LoginView, PasswordResetView,PasswordResetConfirmView,PasswordResetCompleteView
from .views import LogoutView, RegisterView,ProfileView,ImageUpdateView