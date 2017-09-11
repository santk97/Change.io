# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import EmailMessage
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from twilio.rest import Client

from forms import LoginForm, SignUpForm,Indexform1 , swatch_signform , swatch_LoginForm
from models import UserModel, SessionToken,indexmodel , swatch_UserModel

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
            user.is_active=False
            user.save()
            try:

                emaill = EmailMessage('Activation Link', ' HEY...Welcome To CHANGE.IO ....'
                                                         '.click on the link below to get your account activated \n\n '
                                                         'http://127.0.0.1:8000/activate/?email=' +email,
                                      to=[email])
                emaill.send()
                print "email send"
            except:
                print ' network error in sending the mail'

            print ' user saved'
            return render(request, 'activate_link.html')
        else:
            print ' form invalid'
    elif request.method == "GET":
        print ' get called'
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def activate(request):

        print 'Activate called'
        email = request.GET.get('email')
        #name=request.GET.get('name')
        print email
        #print name
        user_object = UserModel.objects.filter(email=email).all()
        print user_object.first()
        user_obj= user_object.first()
        try:
            print  user_obj.name ,  user_obj.is_active

            if user_object:
                if user_obj.is_active == False:
                    user_obj.is_active = True
                    print 'user has been activated'
                    user_obj.save()
                    return HttpResponseRedirect('/login/')
                else:
                    print ' user has been alreay activated'
                    return HttpResponseRedirect('/login/')
            else:
                print ' no user returned'
        except:
            pass
        return render(request, 'login.html',)


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
            if user:
                 if user.is_active==True:
            # message.send()

                # Check for the password
                    if check_password(password, user.password):
                        print 'User is valid'
                        try:

                            emaill = EmailMessage('You just Logged in...',
                                              ' HEY...You just Logged in on for CHANGE.IO ....Report if it was not you'
                                              ,
                                              to=[email])
                            emaill.send()
                            print "email send"
                        except:
                            print ' network error in sending the mail'

                        token = SessionToken(user=user)
                        token.create_token()
                        token.save()
                        response = redirect('/index/')
                        response.set_cookie(key='session_token', value=token.session_token)
                        return response
                    else:
                        print 'User is invalid'
                        response_data['message'] = 'Incorrect Password! Please try again!'
            else:
                print 'user has not been activated'
                response_data['message'] = 'You have not been activated ...Please check your mail!'
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

def swatchh_signup(request):
    print ' swatchh signup view called'
    if request.method == "POST":
        print ' post called'
        form = swatch_signform(request.POST)
        if form.is_valid():
            print ' form is valid'
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']
            print name, email
            user = swatch_UserModel(email=email, name=name, password=make_password(password),
                             re_password=make_password(re_password))
           
            user.save()
            try:

                emaill = EmailMessage('Activation Link', ' HEY...Welcome To Swatch Bharat Abhiyan....',to=[email])
                emaill.send()
                print "email send"
            except:
                print ' network error in sending the mail'

            print ' user saved'
            return HttpResponseRedirect('/swatchh_login/')
        else:
            print ' form invalid'
    elif request.method == "GET":
        print ' get called'
        form = SignUpForm()

    return render(request , 'signup_swachh.html')

def swatch_login(request):
    print 'swatchh loin page called'
    response_data = {}
    if request.method == "POST":
        form = swatch_LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = swatch_UserModel.objects.filter(email=email).first()
            if user:
                if user.is_active == True:
                    # message.send()

                    # Check for the password
                    if check_password(password, user.password):
                        print 'User is valid'
                        try:

                            emaill = EmailMessage('You just Logged in...',
                                                  ' HEY...You just Logged in on for Swatch Bhrata Initiative ....Report if it was not you'
                                                  ,
                                                  to=[email])
                            emaill.send()
                            print "email send"
                        except:
                            print ' network error in sending the mail'

                        token = SessionToken(user=user)
                        token.create_token()
                        token.save()
                        response = redirect('/index/')
                        response.set_cookie(key='session_token', value=token.session_token)
                        return response
                    else:
                        print 'User is invalid'
                        response_data['message'] = 'Incorrect Password! Please try again!'
            else:
                print 'user has not been activated'
                response_data['message'] = 'You have not been activated ...Please check your mail!'
    elif request.method == "GET":
        form = swatch_LoginForm()

    response_data['form'] = form

    return render(request,'login_swachh.html',response_data)



