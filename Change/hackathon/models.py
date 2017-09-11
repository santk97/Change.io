# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

# Create your models here.
class UserModel(models.Model):
  email = models.EmailField()
  name = models.CharField(max_length=120)
  password = models.CharField(max_length=400)
  re_password = models.CharField(max_length=400)
  is_active=models.BooleanField(default=False)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
       return self.name


# post model

class SessionToken(models.Model):
    user = models.ForeignKey(UserModel)
    session_token = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)

    def create_token(self):
        self.session_token = uuid.uuid4()
    def __str__(self):
        return self.user

class project_model(models.Model):
    project_name=models.CharField(max_length=400)

class indexmodel(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)


<<<<<<< HEAD
class startmodel(models.Model):

    
    name=models.CharField(max_length=400)
    age=models.IntegerField(max_length=2)
    link=models.URLField()
    description=models.CharField(max_length=400)
    def __str__(self):
        return self.name
=======
class swatch_UserModel(models.Model):
  email = models.EmailField()
  name = models.CharField(max_length=120)
  password = models.CharField(max_length=400)
  re_password = models.CharField(max_length=400)

  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
       return self.email

>>>>>>> 44c8bef70f1b64cbc791b5e394caef27d71b82de
