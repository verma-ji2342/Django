"""
Admin routes
"""

from django.contrib import admin
from home.models import Person

# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']
