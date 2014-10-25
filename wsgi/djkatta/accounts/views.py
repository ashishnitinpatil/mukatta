from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def index(request):
    """Landing page."""
    return render(request, 'index.html')


def login(request, *args, **kwargs):
    """Login view for User accounts"""
    # Redirects user if already logged in
    if request.user.is_authenticated():
        redir = request.GET.get('next', None)
        if not redir:
            redir = settings.LOGIN_REDIRECT_URL
        return redirect(redir)
    else:
        return render(request, 'accounts/login.html')


@login_required
def home(request):
    """User home"""
    return render(request, 'accounts/home.html')

