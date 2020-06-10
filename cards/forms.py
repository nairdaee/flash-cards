from .models import Profile
from django import forms
from django.forms import ModelForm

class EditProfile(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['userId']

class UpdateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['userId']