from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserUpdateAPIView, UserRetrieveAPIView, UserDestroyAPIView, UserListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', UserListAPIView.as_view(), name='list'),
    path('update/<int:pk>', UserUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='retrieve'),
    path('destroy/<int:pk>', UserDestroyAPIView.as_view(), name='destroy'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
