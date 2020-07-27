from django.contrib import admin
from .models import Profile


# class ProfileAdmin(admin.ModelAdmin):
#     last_display = ['full_name']


admin.site.register(Profile)


