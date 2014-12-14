from django.shortcuts import redirect, render_to_response
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
# from djkatta.roomreq.forms import


@login_required
def index(request):
    """Landing page."""
    return render_to_response('roomreq/index.html', locals(),
                              RequestContext(request))


# @csrf_protect
@login_required
def new_post(request):
    """New roomreq post"""
    return redirect(reverse('roomreq_index'))


@login_required
def my_posts(request):
    """All posts by the user"""
    return redirect(reverse('roomreq_index'))


# @csrf_protect
@login_required
def edit(request):
    """Edit a roomreq post"""
    return redirect(reverse('roomreq_index'))


@login_required
def indi(request):
    """Individual roomreq post view"""
    return redirect(reverse('roomreq_index'))
