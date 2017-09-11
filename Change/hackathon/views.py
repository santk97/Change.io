# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import UserModel,SessionToken,indexmodel
from forms import LoginForm,SignUpForm,Indexform1
from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import render,redirect
import os
from datetime import timedelta
from django.utils import timezone
from django.core.mail import EmailMessage
from twilio.rest import Client

CLIENT_ID='2e8b96d3df82469'
CLIENT_SECRET= 'f6292d93b81e0f055521eb71084b63b9ccc5329d'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
account_sid = "ACcee93f758892db32f0920ab88b1ca945"
auth_token = "144914bd933e248294d546ae74479862"
client = Client(account_sid, auth_token)


def singnup_view(request):
    print ' signup view called'
    if request.method == "POST":
        print ' post called'
        form = SignUpForm(request.POST)
        if form.is_valid():
            print ' form is valid'
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']
            print name , email
            user = UserModel(email=email, name=name,password=make_password(password),re_password=make_password(re_password))

            user.save()
            try:

                emaill = EmailMessage('Activation Link', ' HEY...Welcome To CHANGE.IO ....'
                                                         '.click on the link below to get your account activated \n\n '
                                                         'http://127.0.0.1:8000/activate/?username=' + make_password(name),
                                      to=[email])
                emaill.send()
                print "email send"
            except:
                print ' network error in sending the mail'

            print ' user saved'
            return redirect('/login/')
        else:
            print ' form invalid'
    elif request.method == "GET":
        print ' get called'
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# login function

def login_user(request):
    print 'loin page called'
    response_data = {}
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = UserModel.objects.filter(email=email).first()
            try:

                emaill = EmailMessage('You just Logged in...', ' HEY...You just Logged in on for CHANGE.IO ....Report if it was not you'
                                                         ,
                                      to=[email])
                emaill.send()
                print "email send"
            except:
                print ' network error in sending the mail'


            # message.send()
            if user:
                # Check for the password
                if check_password(password, user.password):
                    print 'User is valid'
                    token = SessionToken(user=user)
                    token.create_token()
                    token.save()
                    response = redirect('/index/')
                    response.set_cookie(key='session_token', value=token.session_token)
                    return response
                else:
                    print 'User is invalid'
                    response_data['message'] = 'Incorrect Password! Please try again!'
    elif request.method == "GET":
        form = LoginForm()

    response_data['form'] = form
    return render(request, 'login.html', response_data)

# post function

def check_validation(request):
    if request.COOKIES.get('session_token'):
        session = SessionToken.objects.filter(session_token=request.COOKIES.get('session_token')).first()
        if session:
            return session.user
    else:
        return None
def logout_view(request):
    user=check_validation(request)
    if user:
        token=SessionToken.objects.filter(user=user)
        token.delete()
        return redirect('/login/')
    else:
        return redirect('/login/')


# Create your views here.
def indexview1(request):
    if request.method == 'POST':
        form = Indexform1(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name= form.cleaned_data['last_name']
            #subject = form.cleaned_data['subject']
            user = indexmodel(first_name=first_name,last_name=last_name)
            user.save()
            try:
                email = form.cleaned_data.get('email')
                emaill = EmailMessage('Feedback', 'New suggestion form' + (first_name),
                                      to=[email])
                emaill.send()
                print "email send"
            except:
                print ' network error in sending the mail'

            return render(request, 'index.html')
        else:
            print " "
    elif request.method == 'GET':
        form = Indexform1()
    return render(request, 'index.html', {'form': form})


