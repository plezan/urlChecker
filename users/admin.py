from django.contrib import admin
from .models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', )
    search_fields = ['username', 'email', ]

admin.site.register(UserProfile, UserProfileAdmin)