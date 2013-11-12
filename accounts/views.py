from django.http import HttpResponse, HttpResponseRedirect
import django.contrib.auth
from django.shortcuts import render

import django.contrib.auth.forms as forms

def check_credentials(request):
    '''
    If request contains correct POSTed username and password,
    create a session for the user and return True, just return
    False otherwise.
    '''
    username = request.POST['username']
    password = request.POST['password']
    user = django.contrib.auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            # Create session.
            django.contrib.auth.login(request, user)
            return True
    return False

def login(request):
    # login is called on GET or on POST for the login page.
    # NOTE: Perhaps this could be split up?
    if request.method == 'POST':
        # Validate form and login user.
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid() and check_credentials(request):
            return HttpResponseRedirect('/')
    else:
        # If user is already logged in, redirect them home.
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        else:
            # Otherwise, create a login form.
            return render(request, 'accounts/login.html', {
                'form': forms.AuthenticationForm()
            }
        )

def register(request):
        return render(request, 'accounts/register.html', {})

def logout(request):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect('/accounts/login/')


