from django import forms
from django.db import models
from django.db.models import fields
from .models import Food


class Foodform(forms.ModelForm):
    class meta:
        model = Food
        fields = ('name', 'text', 'time', 'photo')
