from django.contrib import admin
from .models import PG, PGImage
# Register your models here.
@admin.register(PG)
class PGAdmin(admin.ModelAdmin):
    list_display = ('pg_id', 'name', 'description')
    search_fields = ('name', 'description')

@admin.register(PGImage)
class PGImageAdmin(admin.ModelAdmin):
    list_display = ('pg',)