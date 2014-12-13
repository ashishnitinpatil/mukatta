from django.shortcuts import redirect, render_to_response
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from djkatta.accounts.forms import RegistrationForm, LoginForm


@csrf_protect
def index(request):
    """Landing page."""
    return redirect(reverse('user:login'))


def about(request):
    """About this website"""
    return render_to_response('about.html')
