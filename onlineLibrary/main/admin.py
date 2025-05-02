from django.contrib import admin
from .models import Reader

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'date_of_birth', 'number', 'date_of_registration','is_admin')
    search_fields = ('name', 'surname', 'email')
    list_filter = ('date_of_registration',)
