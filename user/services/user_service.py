from user.models import User
from django.core.mail import send_mail
from django.conf import settings


def create_user(validated_data):
    email = validated_data.pop('email')
    password = validated_data.pop('password')
    
    user = User.objects.create_user(
        email=email,
        password=password,
        **validated_data
    )
    send_verification_email(user)
    return user



def send_verification_email(user):
    token = user.generate_verification_token()
    verification_link = f"{settings.BASE_URL}/user/api/verify-email/?token={token}&uid={user.id}"
    subject = "Verify your email address"
    message = f"Hi {user.first_name},\n\nPlease click the link below to verify your email address:\n\n{verification_link}\n\nThank you!"
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])