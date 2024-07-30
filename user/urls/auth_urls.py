from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.apis.auth_apis import RegisterView, UserListView, VerifyEmailView

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name="register"),
    path('users/', UserListView.as_view(), name='user-list'),
   path('api/verify-email/', VerifyEmailView.as_view(), name='verify_email'),
]

