from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.forms.util import ErrorList
from django.contrib import auth, messages
from django.conf import settings
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime, timedelta
from djkatta.accounts.models import pass_reset_validb
from djkatta.accounts.forms import (
    RegistrationForm, LoginForm, PasswordResetRequestForm,
    PasswordChangeForm, PasswordResetChangeForm
)
from djkatta.accounts.utils import (
    generate_random_string, get_username_from_email, get_email_from_username,
    send_pass_reset_mail, reCaptcha,
)


# template (DRY) for message box rendering
def message_box(request=None, message="Something went wrong.", redir=settings.LOGIN_URL):
    messages.success(request, message)
    return redirect(redir)


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
                usernm = form.cleaned_data['username'].strip()
                if '@' in usernm:
                    usernm = usernm[:usernm.find('@')]
                passwd = form.cleaned_data['password']
                user = auth.authenticate(username=usernm, password=passwd)
                if user and user.is_active:
                    # Correct password, and the user is marked "active"
                    auth.login(request, user)
                    if form.cleaned_data['login_rem']:
                        request.session.set_expiry(7*60*60*24)
                    return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
                else:
                    errors = form._errors.setdefault("username", ErrorList())
                    errors.append("Invalid username or password")
        return render_to_response('accounts/login.html',locals(),RequestContext(request))


@csrf_protect
def register(request):
    form = RegistrationForm()
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            usernm = form.cleaned_data['username'].strip()
            if '@' in usernm:
                usernm = usernm[:usernm.find('@')]
            try:
                user = auth.models.User.objects.get(username__iexact=usernm)
            except:
                user = False
            if user and user.is_active:
                errors = form._errors.setdefault("username", ErrorList())
                errors.append("That username is already registered! "
                              "If you have recently registered, you need to reset your password.")
            elif not usernm:
                errors = form._errors.setdefault("username", ErrorList())
                errors.append("Please enter a valid username.")
            else:
                # check for captcha response
                remote_ip = request.META.get('REMOTE_ADDR', '')
                captcha_response = request.POST.get('g-captcha-response')
                captcha_ok, captcha_msg = reCaptcha(remote_ip,captcha_response)

                if captcha_ok:
                    passwd = generate_random_string()
                    email  = get_email_from_username(usernm)
                    user   = auth.models.User.objects.create_user(
                        username=usernm,
                        password=passwd,
                        email=email,
                        first_name=form.cleaned_data['first_name'].strip(),
                        last_name=form.cleaned_data['last_name'].strip(),
                    )
                    validb = pass_reset_validb.objects.create(username=usernm)
                    send_pass_reset_mail(validb.username, validb.valid_hash, reg=True)
                    message = "Check your Mu Sigma email for further instructions."
                    return message_box(request, message)
                else:
                    errors = form._errors.setdefault("username", ErrorList())
                    errors.append("Invalid captcha request.")
                    errors.append(captcha_msg)
    return render_to_response('accounts/register.html', locals(),
                              RequestContext(request))


def check_mail(request):
    message = "Registration successful! Check your email for further instructions."
    return message_box(request, message)


@login_required
@csrf_protect
def password_change_form(request):
    if not request.POST:
        form = PasswordChangeForm()
        # logging.error('pass change')
        return render_to_response('accounts/password_change_form.html',
                                  locals(), RequestContext(request))
    else:
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            if request.user.check_password(form.cleaned_data['password_old']):
                request.user.set_password(form.cleaned_data['password'])
                request.user.save()
                auth.logout(request)
                return redirect(reverse('user:password_change_success'))
            else:
                # form = PasswordChangeForm()
                form.add_error("password_old", "Original password is incorrect")
        return render_to_response('accounts/password_change_form.html',
                                  locals(), RequestContext(request))


def password_change_success(request):
    return message_box(
        request, 
        "Your password was successfully changed. You have been logged out."
    )


# reset request validation function
def validate_pass_reset_req(username="", given_hash="", delete=False):
    if username and given_hash:
        try:
            reset_req = pass_reset_validb.objects.filter(username=username)[0]
            if delete:
                reset_req.delete()
            else:
                if all((reset_req.valid_hash == given_hash,
                        reset_req.valid_upto >= datetime.today())):
                    return True
        except pass_reset_validb.DoesNotExist:
            return None


@csrf_protect
def password_reset_req(request):
    """Landing page."""
    if request.POST:
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].strip()
            if '@' in username:
                username = username[:username.find('@')]
            try:
                reset_req = pass_reset_validb.objects.get(username=username)
                if reset_req.valid_upto:
                    reset_req.valid_upto = datetime.today() + timedelta(days=1)
                    reset_req.save()
            except pass_reset_validb.DoesNotExist:
                reset_req = pass_reset_validb.objects.create(username=username)
            send_pass_reset_mail(reset_req.username, reset_req.valid_hash)
            message = "Check your Mu Sigma email for further instructions."
            return message_box(request, message)
    else:
        form = PasswordResetRequestForm()
    return render_to_response('accounts/password_reset_req.html', locals(),
                              RequestContext(request))


@csrf_protect
def password_reset_change(request, username="", hash=""):
    if not request.POST:
        form = PasswordResetChangeForm()
        return render_to_response('accounts/password_reset_change.html',
                                  locals(), RequestContext(request))
    else:
        form = PasswordResetChangeForm(request.POST)
        if form.is_valid():
            try:
                if validate_pass_reset_req(username, hash):
                    user = auth.models.User.objects.get(username=username)
                    user.set_password(form.cleaned_data['password'])
                    user.save()
                    # delete the reset request entry
                    validate_pass_reset_req(username, hash, delete=True)
                    return message_box(
                        request,
                        "Your password was successfully reset!"
                    )
                # invalid request, raise error & trigger exception
                raise pass_reset_validb.DoesNotExist
            except pass_reset_validb.DoesNotExist:
                form.add_error("password", "Invalid reset request hash")
                form.add_error("password_re", "Invalid reset request hash")
        return render_to_response('accounts/password_reset_change.html',
                                  locals(), RequestContext(request))


def password_reset_success(request):
    return message_box(request, "Your password was successfully reset!")


@login_required
def indi(request, username=""):
    if username:
        try:
            user = auth.models.User.objects.get(username=username)
        except auth.models.User.DoesNotExist:
            user = None
    return render_to_response('accounts/indi.html',
                              locals(), RequestContext(request))


@login_required
def index(request):
    return redirect(reverse('user:indi', kwargs={'username':request.user.username}))
