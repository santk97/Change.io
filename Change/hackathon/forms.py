

from models import UserModel,project_model , indexmodel,startmodel
from models import UserModel,project_model , LikeModel,indexmodel ,swatch_UserModel


from models import UserModel,project_model , indexmodel ,swatch_UserModel , feedback_model

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
        fields=['name','sex','age','theme','country','link','description']

class swatch_signform(forms.ModelForm):
    class Meta:
        model=swatch_UserModel
        fields = ['email', 'name', 'password', 're_password']

class swatch_LoginForm(forms.ModelForm):
    class Meta:
      model = swatch_UserModel
      fields = ['email', 'password']


class LikeForm(forms.ModelForm):
  class Meta:
    model = LikeModel
    fields = ['post']

class feedback_form(forms.ModelForm):
    class Meta:
        model=feedback_model
        fields=['first_name','last_name','subject']

class password_form(forms.ModelForm):
    class Meta:
        model=UserModel
        fields=['password','re_password']

