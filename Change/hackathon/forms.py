from models import UserModel,project_model
from django import forms

class SignUpForm(forms.ModelForm):
  class Meta:
    model = UserModel
    fields=['email','name','password','re_password']




class LoginForm(forms.ModelForm):
    class Meta:
      model = UserModel
      fields = ['email', 'password']
