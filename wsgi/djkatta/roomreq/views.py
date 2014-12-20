from django.shortcuts import redirect, render_to_response
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from djkatta.roomreq.forms import RoomReqForm
from djkatta.roomreq.models import get_next_month_first_date
from django.contrib import messages
from djkatta.roomreq.models import room_requirement


@login_required
def index(request):
    """Landing page."""
    posts = room_requirement.active.all()
    for post in posts:
        post.url = post.get_post_url()
        if post.owner.id == request.user.id:
            post.editable = True
        else:
            post.editable = False
        post.gender_cont = ""
        if post.gender_req == "M":
            post.gender_cont = "male"
        elif post.gender_req == "F":
            post.gender_cont = "female"
        post.gender_plural = ""
        if post.vacancies > 1:
            post.gender_plural = "s"
    return render_to_response('roomreq/index.html', locals(),
                              RequestContext(request))


@csrf_protect
@login_required
def new_post(request):
    """New roomreq post"""
    disp_date = get_next_month_first_date().strftime("%Y-%m-%d")
    form = RoomReqForm(request.POST)
    if form.is_valid():
        cur_post = form.save(commit=False)
        cur_post.owner = request.user
        cur_post = form.save()
        messages.success(request, 'Post submission was successful!')
        return redirect(cur_post.get_post_url())
    return render_to_response('roomreq/new_post.html', locals(), RequestContext(request))


@login_required
def my_posts(request):
    """All posts by the user"""
    posts = room_requirement.objects.filter(owner=request.user)
    for post in posts:
        post.url = post.get_post_url()
    return render_to_response('roomreq/my_posts.html', locals(), RequestContext(request))


@csrf_protect
@login_required
def edit(request, post_id=None):
    """Edit a roomreq post"""
    allowed = False
    does_not_exist = False
    try:
        cur_post = room_requirement.objects.get(id=post_id)
        if cur_post.owner == request.user:
            allowed = True
    except room_requirement.DoesNotExist:
        cur_post = None
        does_not_exist = True
        messages.warning(request, 'You have wandered off!')
    # process only if post exists & edit is allowed
    if cur_post and allowed:
        form = RoomReqForm(instance=cur_post)
        if cur_post.req_open == "C":
            post_open = False
        else:
            post_open = True
        gender_m = gender_f = gender_a = False
        if cur_post.gender_req == "M":
            gender_m = True
        elif cur_post.gender_req == "F":
            gender_f = True
        else:
            gender_a = True
        cur_post_url = cur_post.get_post_url()
        if request.POST:
            form = RoomReqForm(request.POST)
            cur_post.owner = request.user
            if form.is_valid():
                cur_post = form.save(commit=False)
                cur_post.owner = request.user
                cur_post.id = post_id
                cur_post.save()
                messages.info(request, 'Post successfully updated.')
                return redirect(cur_post_url)
            logging.error(form.errors)
    return render_to_response('roomreq/edit_post.html', locals(), RequestContext(request))


@login_required
def indi(request, post_id=None):
    """Individual post view"""
    try:
        cur_post = room_requirement.objects.get(id=post_id)
        if cur_post.req_open == "O":
            active = True
        else:
            active = False
        if cur_post.gender_req == "M":
            cur_post.gender_cont = "Males only"
        elif cur_post.gender_req == "F":
            cur_post.gender_cont = "Females only"
        else:
            cur_post.gender_cont = "Any"
        cur_post_url = cur_post.get_post_url()
        if cur_post.owner == request.user:
            cur_post.editable = True
        else:
            cur_post.editable = False
    except room_requirement.DoesNotExist:
        cur_post = None
        messages.warning(request, 'You have wandered off!')
    return render_to_response('roomreq/indi.html', locals(), RequestContext(request))
