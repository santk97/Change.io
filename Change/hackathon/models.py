# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

# Create your models here.
class UserModel(models.Model):
  email = models.EmailField()
  username = models.CharField(max_length=120)
  password = models.CharField(max_length=400)
  re_password = models.CharField(max_length=400)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  def __str__(self):
       return self.username


# post model

class SessionToken(models.Model):
    user = models.ForeignKey(UserModel)
    session_token = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)

    def create_token(self):
        self.session_token = uuid.uuid4()

class indexmodel(models.Model):

    first_name=models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    #subject= models.CharField(max_length=400)

    def __str__(self):
        self.first_name
