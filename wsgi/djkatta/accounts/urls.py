"""
Urls for the djkatta.accounts app.

Why should we have multiple urls.py?!
http://stackoverflow.com/a/9324559/2689986
"""

from django.conf.urls import patterns, url
from django.contrib.auth.views import logout
from django.conf import settings

# App specific URL patterns
urlpatterns = patterns("djkatta.accounts.views",

    # Login & Logout
    url(r'login/$', 'login', name='login'),
    url(r'logout/$', logout, {'template_name': 'accounts/logout.html',
                              'next_page': settings.LOGIN_REDIRECT_URL},
                             name='logout'),
    url(r'register/$', 'register', name='register'),
    url(r'check_mail/$', 'check_mail', name='check_mail'),
    url(r'password_reset_form/$', 'password_change_form', name='password_change_form'),
    url(r'password_reset_req/$', 'password_reset_req', name='password_reset_req'),
    url(r'password_reset_success/$', 'password_reset_success', name='password_reset_success'),
)
