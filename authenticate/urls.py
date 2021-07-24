from django.urls import path
from .views import RegisterView, LoginView
from rest_framework.authtoken import views


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='register'),
    path('api-token-auth/', views.obtain_auth_token)
]
