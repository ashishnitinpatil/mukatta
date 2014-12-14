from django.conf.urls import patterns, url

# App specific URL patterns
urlpatterns = patterns("djkatta.roomreq.views",

    # post new req
    url(r'new_post/$', 'new_post', name='new_post'),

    # view posts by the user
    url(r'my_posts/$', 'my_posts', name='my_posts'),

    # modify old req
    url(r'(?P<post_id>[\d]+)/edit/$', 'edit', name='edit'),

    # view individual req
    url(r'(?P<post_id>[\d]+)/$', 'indi', name='indi'),
)
