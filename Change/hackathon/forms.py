

from django import forms

from models import UserModel, swatch_UserModel, feedback_model
from models import startmodel


class SignUpForm(forms.ModelForm):
  class Meta:
    model = UserModel
    fields=['email','name','password','re_password']




class LoginForm(forms.ModelForm):
    class Meta:
      model = UserModel
      fields = ['email', 'password']


class Startform(forms.ModelForm):
    class Meta:
        model=startmodel
        fields=['name','sex','age','theme','country','link','description']

class swatch_signform(forms.ModelForm):
    class Meta:
        model=swatch_UserModel
        fields = ['email', 'name', 'password', 're_password']

class swatch_LoginForm(forms.ModelForm):
    class Meta:
      model = swatch_UserModel
      fields = ['email', 'password']




class feedback_form(forms.ModelForm):
    class Meta:
        model=feedback_model
        fields=['first_name','last_name','subject']

class password_form(forms.ModelForm):
    class Meta:
        model=UserModel
        fields=['password','re_password']

