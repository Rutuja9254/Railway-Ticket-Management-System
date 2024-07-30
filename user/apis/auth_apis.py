from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from user.serializers.auth_serializers import RegisterSerializer, UserSerializer
from user.services.user_service import create_user
from rest_framework.views import APIView
from user.models import User
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user(serializer.validated_data)
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
    
class VerifyEmailView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        token = request.query_params.get('token')
        uid = request.query_params.get('uid')
        try:
            user = User.objects.get(pk=uid)
            if default_token_generator.check_token(user, token):
                user.is_verified = True
                user.save()
                return Response({"message": "Email verified successfully!"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid token or user ID."}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)