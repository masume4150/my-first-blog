from django.contrib import admin
from .models import Food
# Register your models here.


@admin.register(Food)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'time', 'photo')
