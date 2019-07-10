from django.conf.urls import url 
from django.contrib.auth.views import LoginView, PasswordResetView,PasswordResetConfirmView,PasswordResetCompleteView
from .views import LogoutView, RegisterView,ProfileView,ImageUpdateView

urlpatterns = [
    url('login/', LoginView.as_view(), name='login'),
    url('logout/', LogoutView.as_view(), name='logout'),
    url('register/', RegisterView.as_view(), name='register'),
    url('password_reset/', PasswordResetView.as_view(), name='password_reset'),
#     url('password_reset/done/', PasswordResetDoneView.as_view(),
     #     name='password_reset_done'),
    url('password_reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url('password_reset/complete/', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    url('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    url('profile/picture/', ImageUpdateView.as_view(), name='update_image'),
]
