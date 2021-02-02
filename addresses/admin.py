from django.contrib import admin

from .models import Address

# Register your models here.

class WebAddress(admin.ModelAdmin):
    list_display = ('url','name')
    search_fields = ['name', 'url']

admin.site.register(Address, WebAddress)
