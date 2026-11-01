from django.contrib import admin
from .models import Profile, PasswordResetOTP
# Register your models here.
admin.site.register(Profile)
admin.site.register(PasswordResetOTP)