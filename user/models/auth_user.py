from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from user.managers.user_manager import UserManager
from django.contrib.auth.tokens import default_token_generator

#gender choices
MALE = "M"
FEMALE = "F"
OTHER = "O"
GENDER_CHOICES = [
    (MALE, "Male"),
    (FEMALE, "Female"),
    (OTHER, "Other"),
]

#identity choices
AADHAAR = "A"
PAN = "P"
VOTER= "V"
IDENTITY_TYPE_CHOICES = [
    (AADHAAR, "Aadhaar"),
    (PAN, "Pan Card"),
    (VOTER, "Voter Id"),
]

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    identity_type = models.CharField(max_length=50,choices=IDENTITY_TYPE_CHOICES, default=AADHAAR)
    identity_number = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def generate_verification_token(self):
        return default_token_generator.make_token(self)

    def __str__(self):
        return self.email