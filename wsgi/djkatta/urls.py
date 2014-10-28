from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('djkatta.accounts.views',
    # Django admin urls
    url(r'^admin/', include(admin.site.urls)),

    # Landing page - /
    url(r"^$", "index", name="index"),

    # Home page - /home
    url(r"^home/$", "home", name="home"),

    # "accounts" app urls
    url(r'^user/', include("djkatta.accounts.urls", namespace='user')),
)
