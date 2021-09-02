from django import forms

from .models import AboutUs


class PostForm(forms.ModelForm):

    class Meta:
        model = AboutUs
        fields = ('home', 'call',)
