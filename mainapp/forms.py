from django import forms
from .models import*
from django.contrib.auth.models import User

class Registration_form(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'User Name'}), max_length=20, required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}), max_length=30, required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}), max_length=30, required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Address'}), max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}), max_length=30, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}), max_length=30, required=True)

    class Meta():
        model = User
        fields=['username','first_name','last_name','email','password']

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageUploader
        fields = '__all__'
        labels = {'photo':''}
