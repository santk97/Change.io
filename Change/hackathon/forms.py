from models import UserModel
from django import forms

class SignUpForm(forms.ModelForm):
  class Meta:
    model = UserModel
    fields=['email','username','name','password']

class LoginForm(forms.ModelForm):
    class Meta:
      model = UserModel
      fields = ['username', 'password']
