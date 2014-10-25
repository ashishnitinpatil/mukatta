"""
Urls for the djkatta.apkatta app.

Why should we have multiple urls.py?!
http://stackoverflow.com/a/9324559/2689986
"""

from django.conf.urls import patterns, url

# App specific URL patterns
urlpatterns = patterns("djkatta.apkatta.views",
    # Landing page - /
    url(r"^$", "index", name="index"),

    # Home page - /home
    url(r"^home/$", "home", name="home"),
)
