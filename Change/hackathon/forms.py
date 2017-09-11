<<<<<<< HEAD
from models import UserModel,project_model , indexmodel,startmodel
=======
from models import UserModel,project_model , indexmodel ,swatch_UserModel
>>>>>>> 44c8bef70f1b64cbc791b5e394caef27d71b82de
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

<<<<<<< HEAD

class Startform(forms.ModelForm):
    class Meta:
        mode=startmodel
        fields=['name','sex','age','theme','link','description']
=======
class swatch_signform(forms.ModelForm):
    class Meta:
        model=swatch_UserModel
        fields = ['email', 'name', 'password', 're_password']

class swatch_LoginForm(forms.ModelForm):
    class Meta:
      model = swatch_UserModel
      fields = ['email', 'password']
>>>>>>> 44c8bef70f1b64cbc791b5e394caef27d71b82de
