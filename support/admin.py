from django.contrib import admin
from support.models import Support

class SupportAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'timestamp')
    list_filter = ('email', 'phone_number')
