from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView


urlpatterns = patterns('',
    # Django admin urls
    url(r'^admin/', include(admin.site.urls)),

    # Landing page - /
    url(r"^$", "djkatta.views.index", name="index"),

    # About page - /about
    url(r"^about/$", "djkatta.views.about", name="about"),

    # Robots page - /robots.txt
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt',
        content_type='text/plain'), name="robots"),
    # Favicon - /favicon.ico
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.png'),
        name="favicon"),

    # "accounts" app urls
    url(r'^user/', include("djkatta.accounts.urls", namespace='user')),
    url(r'^user/$', 'djkatta.accounts.views.index', name='user_index'),

    # "cabshare" app urls
    url(r'^cabshare/', include("djkatta.cabshare.urls", namespace='cabshare')),
    url(r'^cabshare/$', 'djkatta.cabshare.views.index', name="cabshare_index"),

    # "roomreq" app urls
    url(r'^roomreq/', include("djkatta.roomreq.urls", namespace='roomreq')),
    url(r'^roomreq/$', 'djkatta.roomreq.views.index', name="roomreq_index"),
)
