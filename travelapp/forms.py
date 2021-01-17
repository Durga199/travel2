from django import forms
from .models import *
class register1(forms.ModelForm):
    class Meta:
        model = register
        fields = ['username', 'dob', 'mobile', 'address','gender', 'nationality','image']