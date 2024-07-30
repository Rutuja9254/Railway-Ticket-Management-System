from django.contrib import admin
from .models.auth_user import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')

admin.site.register(User, UserAdmin)