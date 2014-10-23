#!/usr/bin/env python
from django.db import models
from django.conf import settings
from django.contrib.auth import models as auth_models
from django.db.models import signals

# Create our own root user automatically.

def create_rootuser(app, created_models, verbosity, **kwargs):
  if not settings.DEBUG:
    return
  try:
    auth_models.User.objects.get(username='root')
  except auth_models.User.DoesNotExist:
    print '*' * 80
    print 'Creating "root" user -- login: root, password: root'
    print '*' * 80
    assert auth_models.User.objects.create_superuser(
        'root',
        'ashishnitinpatil@gmail.com',
        'root'
    )
  else:
    print '"root" user already exists.'

signals.post_syncdb.connect(
    create_rootuser,
    sender=auth_models,
    dispatch_uid='common.models.create_rootuser'
)
