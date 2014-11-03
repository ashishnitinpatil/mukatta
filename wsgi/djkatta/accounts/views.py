from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.forms.util import ErrorList
from django.contrib import auth
from django.conf import settings
from django.http import HttpResponseRedirect
from django.template import RequestContext
from djkatta.accounts.forms import RegistrationForm, LoginForm
from djkatta.accounts.utils import (
    generate_random_string, get_username_from_email, get_email_from_username,
    send_reg_mail,
)
import logging, pprint


@csrf_protect
def index(request):
    """Landing page."""
    login_form = LoginForm(request.POST)
    reg_form = RegistrationForm(request.POST)
    return render_to_response('index.html', locals(), RequestContext(request))


@csrf_protect
def login(request, *args, **kwargs):
    """Login view for User accounts"""
    # Redirects user if already logged in
    if request.user.is_authenticated():
        redir = request.GET.get('next', None)
        if not redir:
            redir = settings.LOGIN_REDIRECT_URL
        return redirect(redir)
    else:
        form = LoginForm()
        if request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
                logging.error("in form valid")
                usernm = form.cleaned_data['username']
                passwd = form.cleaned_data['password']
                user = auth.authenticate(username=usernm, password=passwd)
                if user is not None and user.is_active:
                    # Correct password, and the user is marked "active"
                    auth.login(request, user)
                    if form.cleaned_data['login_rem']:
                        request.session.set_expiry(7*60*60*24)
                    return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
            # logging.error(pprint.pprint([request.POST,form.cleaned_data]))
        # else
        return render_to_response('accounts/login.html',locals(),RequestContext(request))


@login_required
def home(request):
    """User home"""
    return render_to_response('accounts/home.html',{},RequestContext(request))


@csrf_protect
def register(request):
    form = RegistrationForm()
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            usernm = form.cleaned_data['username']
            try:
                user = auth.models.User.objects.get(username__iexact=usernm)
            except:
                user = False
            if user and user.is_active:
                errors = form._errors.setdefault("username", ErrorList())
                errors.append("That username is already registered!"
                              "Forgot password?!")
            else:
                passwd = generate_random_string()
                email  = get_email_from_username(usernm)
                user   = auth.models.User.objects.create_user(
                    username=usernm,
                    password=passwd,
                    email=email,
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                )
                # send_reg_mail(email, usernm, passwd)
                return redirect(reverse('user:check_mail'))
    # else
    return render_to_response('accounts/register.html', locals(),RequestContext(request))


def check_mail(request):
    return render_to_response('accounts/check_mail.html')
