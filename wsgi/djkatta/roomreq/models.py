from django.db import models
from django.contrib.auth import models as auth_models
from djkatta.accounts.models import hash_len


class room_requirement(models.Model):
    """Model to save any room requirement details"""

    owner = models.ForeignKey(auth_models.User, on_delete=models.PROTECT)

    # gender_req choice male, female, any
    # location choice djnago-autocomplete-light
    # rent int amount
    # house_description text descr
    # vacancies int choice 1-6
    # how_many_in_a_room choice 1, 2, 3, 4
    # amenities
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
