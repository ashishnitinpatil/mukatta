from django.shortcuts import redirect, render_to_response
# from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from djkatta.cabshare.forms import CabShareForm
from djkatta.cabshare.models import cab_sharing
import logging


@login_required
def index(request):
    """App home page"""
    posts = cab_sharing.active.all()[:10]
    return render_to_response('cabshare/index.html', locals(), RequestContext(request))


@login_required
def my_posts(request):
    """User home"""
    posts = cab_sharing.objects.filter(owner=request.user)
    return render_to_response('cabshare/my_posts.html', locals(), RequestContext(request))


@csrf_protect
@login_required
def new_post(request):
    """New post"""
    form = CabShareForm(request.POST)
    if form.is_valid():
        cur_post = form.save(commit=False)
        cur_post.owner = request.user
        cur_post = form.save()
        return redirect(cur_post.get_post_url())
    return render_to_response('cabshare/new_post.html', locals(), RequestContext(request))


@login_required
def indi(request, post_id=None):
    """Individual post view"""
    try:
        cur_post = cab_sharing.objects.get(id=post_id)
    except cab_sharing.DoesNotExist:
        cur_post = None
    return render_to_response('cabshare/indi.html', locals(), RequestContext(request))


@csrf_protect
@login_required
def edit(request, post_id=None):
    """Individual post edit"""
    allowed = False
    does_not_exist = False
    try:
        cur_post = cab_sharing.objects.get(id=post_id)
        if cur_post.owner == request.user:
            allowed = True
    except cab_sharing.DoesNotExist:
        logging.error("dne")
        cur_post = None
        does_not_exist = True
    # process only if post exists & edit is allowed
    if cur_post and allowed:
        form = CabShareForm(instance=cur_post)
        cur_post_url = cur_post.get_post_url()
        if request.POST:
            form = CabShareForm(request.POST)
            cur_post.owner = request.user
            if form.is_valid():
                cur_post = form.save(commit=False)
                cur_post.owner = request.user
                cur_post = form.save()
                return redirect(cur_post_url)
    return render_to_response('cabshare/edit_post.html', locals(), RequestContext(request))
