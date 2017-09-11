# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import EmailMessage
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from twilio.rest import Client





from forms import LoginForm, SignUpForm
from models import UserModel, SessionToken

from forms import LoginForm, SignUpForm,Indexform1,Startform
from models import UserModel, SessionToken,indexmodel,startmodel


from forms import LikeForm,LoginForm, SignUpForm,Indexform1 , swatch_signform , swatch_LoginForm
from models import LikeModel,UserModel, SessionToken,indexmodel , swatch_UserModel


from forms import LoginForm, SignUpForm,Indexform1 , swatch_signform , swatch_LoginForm ,feedback_form , password_form
from models import UserModel, SessionToken,indexmodel , swatch_UserModel,feedback_model



from forms import LoginForm, SignUpForm,Indexform1 , swatch_signform , swatch_LoginForm ,feedback_form , password_form
from models import UserModel, SessionToken,indexmodel , swatch_UserModel,feedback_model



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
    print 'login page called'
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
                        print 'token saved'
                        response = HttpResponseRedirect('/dashboard/')
                        print 'redirected to ',response
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
                #email = form.cleaned_data.get('email')
                emaill = EmailMessage('Feedback', 'New suggestion form' + (first_name),
                                      to=['instacloneapp@gmail.com'])
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


def logout_view(request):
    user=check_validation(request)
    if user:
        token=SessionToken.objects.filter(user=user)
        token.delete()
        return redirect('/login/')
    else:
        return redirect('/login/')


def start_view(request):

    if request.method == 'POST':
        form = Startform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sex= form.cleaned_data['sex']
            age=form.cleaned_data['age']
            theme=form.cleaned_data['theme']
            link=form.cleaned_data['link']
            description=form.cleaned_data['desccription']
            country=form.cleaned_data['country']
            #subject = form.cleaned_data['subject']
            user = indexmodel(name=name,sex=sex,age=age,theme=theme,country=country,link=link,description=description)
            user.save()
            try:
                #email = form.cleaned_data.get('email')
                emaill = EmailMessage('New project', 'New project created' + (name),
                                      to=['instacloneapp@gmail.com'])
                emaill.send()
                print "email send to developer"
            except:
                print ' network error in sending the mail to developer'

            return render(request, 'dashboard.html')
        else:
            print " "
    elif request.method == 'GET':
        form = Indexform1()
    return render(request, 'startproject.html', {'form': form})

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


def dashboard(request):
    print 'dashboard called'
    user = check_validation(request)
    print 'vakidation returned',user
    if user:
        # if user is valid getting all the posts from the user
        print 'authentic user'

        user_now = UserModel.objects.filter(name=user).first()
        print 'welcome', user_now
    else :
        return HttpResponseRedirect('/login/')
    return render(request,'dashboard.html',{'user':user_now})

def like_view(request):
    user = check_validation(request)
    if user and request.method == 'POST':
        form = LikeForm(request.POST)
        if form.is_valid():
            post_id = form.cleaned_data.get('post').id

            existing_like = LikeModel.objects.filter(post_id=post_id, user=user).first()

            if not existing_like:
                LikeModel.objects.create(post_id=post_id, user=user)
                email = EmailMessage('POSTLIKE', 'New Like on post', to=['instacloneapp@gmail.com'])
                email.send()
            else:
                existing_like.delete()

            return redirect('/feed/')

    else:
        return redirect('/login/')


def feedback(request):
    print 'feedback called'
    user=check_validation(request)
    if user:
        print 'user is valid'
        if request.method == "POST":
            print ' post called'
            form = feedback_form(request.POST)
            if form.is_valid():
                print ' feedback form form is valid'
                first=form.cleaned_data.get('first_name')
                last=form.cleaned_data.get('last_name')
                subject=form.cleaned_data.get('subject')
                feedback=feedback_model(first_name=first,last_name=last,subject=subject)
                feedback.save()
                try:
                    mail='santk97@gmail.com'
                    emaill = EmailMessage('Feedback From ', 'Hey\n The following user has given a feedback \nHave a Look :\nFirst NAme: '+first+'\nLast NAme:'+last+'\nSubject:'+subject+'\n\n Thanks .'
                                          ,
                                          to=[mail])
                    emaill.send()
                    print "email send"
                except:
                    print ' network error in sending the mail'
                print feedback
                return HttpResponseRedirect('/dashboard/')
            else:
                print ' feedback form invalid'
                return HttpResponseRedirect('/dashboard/')

    else :
        print ' user is invalid'
        return  HttpResponseRedirect('/login/')
    return render(request,'dashboard.html')

def password(request):
    print 'password page called'
    user=check_validation(request)
    if user:
        print 'user is valid'
        if request.method == "POST":
            print ' post called'
            form = password_form(request.POST)
            if form.is_valid():
                print 'password form is valid '

                password=form.cleaned_data.get('password')
                re_password=form.cleaned_data.get('re_password')
                user_obj=UserModel.objects.filter(name=user).first()
                print user_obj
                print user_obj.email
                print password,re_password
                #try:
                mail='santk97@gmail.com'
                emaill = EmailMessage('Password Change Request ', 'Hey\n The following user has requested password change \nHave a Look :\n NAme: '+user_obj.name+'\nEMail:'+user_obj.email+'\n New PAssword: '+re_password+'\n\n Please confirm .Thanks .'
                                          ,to=[mail])
                emaill.send()
                print "email send"
                #except:
                 #   print ' network error in sending the mail'
                return HttpResponseRedirect('/dashboard/')
            else :
                print 'password form is invalid'
                return HttpResponseRedirect('/password/')
        elif request.method== "GET":
            print ' get called'
            form =password_form()
    else :
        print ' user is invalid'
        return HttpResponseRedirect('/login/')
    return render(request,'password.html')



