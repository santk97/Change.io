from models import UserModel,project_model , indexmodel,startmodel
from django import forms

class SignUpForm(forms.ModelForm):
  class Meta:
    model = UserModel
    fields=['email','name','password','re_password']


class Indexform1(forms.ModelForm):
    class Meta:
        model=indexmodel
        fields=['first_name','last_name']

class LoginForm(forms.ModelForm):
    class Meta:
      model = UserModel
      fields = ['email', 'password']


class Startform(forms.ModelForm):
    class Meta:
        mode=startmodel
        fields=['name','sex','age','theme','link','description']