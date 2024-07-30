from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'age', 'gender', 'identity_type', 'identity_number', 'created_at', 'updated_at')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone_number', 'age', 'gender', 'identity_type', 'identity_number')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email address not found.")
        return value
    

class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        new_password = attrs.get('new_password')
        confirm_password = attrs.get("confirm_password")
        if new_password != confirm_password:
            raise serializers.ValidationError("password must match")
        return attrs