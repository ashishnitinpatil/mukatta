from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Django admin urls
    url(r'^admin/', include(admin.site.urls)),

    # Landing page - /
    url(r"^$", "djkatta.views.index", name="index"),

    # Home page - /home
    url(r"^home/$", "djkatta.views.home", name="home"),

    # "accounts" app urls
    url(r'^user/', include("djkatta.accounts.urls", namespace='user')),
)
