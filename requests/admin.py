from django.contrib import admin
from .models import Requests

@admin.register(Requests)
class RequestsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'phone_number', 'date')
    search_fields = ('name', 'phone_number', 'date')
