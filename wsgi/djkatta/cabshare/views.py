from django.shortcuts import redirect, render_to_response
# from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from djkatta.cabshare.forms import CabShareForm
from djkatta.cabshare.models import cab_sharing
from django.contrib import messages
import datetime
# import logging


@login_required
def index(request):
    """App home page"""
    posts = cab_sharing.active.all()
    for post in posts:
        post.url = post.get_post_url()
        if post.owner.id == request.user.id:
            post.editable = True
        else:
            post.editable = False
    return render_to_response('cabshare/index.html', locals(), RequestContext(request))


@login_required
def my_posts(request):
    """All posts by the user"""
    posts = cab_sharing.objects.filter(owner=request.user)
    for post in posts:
        post.url = post.get_post_url()
    return render_to_response('cabshare/my_posts.html', locals(), RequestContext(request))


@csrf_protect
@login_required
def new_post(request):
    """New post"""
    disp_date = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime("%Y-%m-%d")
    form = CabShareForm(request.POST)
    if form.is_valid():
        cur_post = form.save(commit=False)
        cur_post.owner = request.user
        cur_post = form.save()
        messages.success(request, 'Post submission was successful!')
        return redirect(cur_post.get_post_url())
    return render_to_response('cabshare/new_post.html', locals(), RequestContext(request))


@login_required
def indi(request, post_id=None):
    """Individual post view"""
    try:
        cur_post = cab_sharing.objects.get(id=post_id)
        if cur_post.req_open == "O":
            active = True
        else:
            active = False
        cur_post_url = cur_post.get_post_url()
        if cur_post.owner == request.user:
            cur_post.editable = True
        else:
            cur_post.editable = False
    except cab_sharing.DoesNotExist:
        cur_post = None
        messages.warning(request, 'You have wandered off!')
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
        cur_post = None
        does_not_exist = True
        messages.warning(request, 'You have wandered off!')
    # process only if post exists & edit is allowed
    if cur_post and allowed:
        form = CabShareForm(instance=cur_post)
        if cur_post.req_open == "C":
            post_open = False
        else:
            post_open = True
        cur_post_url = cur_post.get_post_url()
        if request.POST:
            form = CabShareForm(request.POST)
            cur_post.owner = request.user
            if form.is_valid():
                cur_post = form.save(commit=False)
                cur_post.id = post_id
                cur_post.owner = request.user
                cur_post.save()
                messages.info(request, 'Post successfully updated.')
                return redirect(cur_post_url)
    return render_to_response('cabshare/edit_post.html', locals(), RequestContext(request))
