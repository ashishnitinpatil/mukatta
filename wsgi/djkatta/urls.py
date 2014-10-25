from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djkatta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Django admin urls
    url(r'^admin/', include(admin.site.urls)),

    
    # Landing page - /
    url(r"^$", "djkatta.accounts.views.index", name="index"),

    # Home page - /home
    url(r"^home/$", "djkatta.accounts.views.home", name="home"),

    # "accounts" app urls
    url(r'^/user', include("djkatta.accounts.urls")),
)
