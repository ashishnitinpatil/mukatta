from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djkatta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Django admin urls
    url(r'^admin/', include(admin.site.urls)),
    # App apkatta urls
    url(r'^/', include(apkatta.urls)),
)
