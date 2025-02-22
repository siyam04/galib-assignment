from django.urls import path

from .views import CustomUserRegistrationView


urlpatterns = [
    path('register', CustomUserRegistrationView.as_view(), name='user-register')
]
