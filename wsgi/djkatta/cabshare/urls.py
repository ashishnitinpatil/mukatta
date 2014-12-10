from django.conf.urls import patterns, url

# App specific URL patterns
urlpatterns = patterns("djkatta.cabshare.views",

    # post new req
    url(r'new_post/$', 'new_post', name='new_post'),

    # view posts by the user
    url(r'my_posts/$', 'my_posts', name='my_posts'),

    # view individual req
    url(r'(?P<post_id>[\w]+)/$', 'indi', name='indi'),

    # modify old req
    url(r'(?P<post_id>[\w]+)/edit/$', 'edit', name='edit'),

    # app main page
    url(r'$', 'index', name='index'),
)
