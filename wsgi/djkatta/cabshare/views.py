from django.shortcuts import redirect, render_to_response
# from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from djkatta.cabshare.forms import CabShareForm
from djkatta.cabshare.models import cab_sharing


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
    new = True
    allowed = True
    form = CabShareForm(request.POST)
    form.owner = request.user
    if form.is_valid():
        cur_post = form.save()
        return redirect(cur_post.get_post_url())
    return render_to_response('cabshare/new_post.html', locals(), RequestContext(request))


@login_required
def indi(request, post_id=None):
    """Individual post view"""
    try:
        cur_post = cab_sharing.objects.get(id=post_id)
    except cur_post.DoesNotExist:
        cur_post = None
    return render_to_response('cabshare/indi.html', locals(), RequestContext(request))


@csrf_protect
@login_required
def edit(request, post_id=None):
    """Individual post edit"""
    new = False
    allowed = True
    try:
        cur_post = cab_sharing.objects.get(id=post_id)
        if not cur_post.owner == request.user:
            allowed = False
    except cur_post.DoesNotExist:
        cur_post = None
    form = CabShareForm(cur_post)
    if request.POST:
        form = CabShareForm(request.POST)
        form.owner = request.user
        if form.is_valid():
            cur_post = form.save()
            return redirect(cur_post.get_post_url())
    return render_to_response('cabshare/new_post.html', locals(), RequestContext(request))
