from django import forms
from .models import Profile,Product,Comment
from django.contrib.auth.models import User

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class SubmitProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['owner','pub_date','profile']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user','image','posted_on']