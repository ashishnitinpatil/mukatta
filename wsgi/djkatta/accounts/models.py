#!/usr/bin/env python
from django.db import models
from django.conf import settings
from django.contrib.auth import models as auth_models
from datetime import datetime, timedelta
from djkatta.accounts.utils import (
    generate_random_string, send_pass_reset_mail
)


hash_len = 16

class pass_reset_validb(models.Model):
    username   = models.CharField(max_length=32)
    valid_hash = models.CharField(max_length=hash_len)
    valid_upto = models.DateTimeField()

    def save(self, *args, **kwargs):
        """Set valid_hash & expiration time for reset request"""

        if not self.valid_hash:
            self.valid_hash = generate_random_string(hash_len)
        if not self.valid_upto:
            # set valid_upto (expiration time) as 1 day from saving request
            self.valid_upto = datetime.today() + timedelta(days=1)
        return super(pass_reset_validb, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = "Password Reset Hashtable"


### The following code is openshift specific (required since no auto syncdb)
# Create our own root user automatically...
# Remember to change the password manually!

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

models.signals.post_syncdb.connect(
    create_rootuser,
    sender=auth_models,
    dispatch_uid='common.models.create_rootuser'
)
### End of openshift specific code
