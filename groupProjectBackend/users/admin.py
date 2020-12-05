from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, HostUser, HeroUser
from .serializers import CustomUserSerializer, CustomUserDetailSerializer

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(HostUser)
admin.site.register(HeroUser)
