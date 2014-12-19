from django.db import models
from django.contrib.auth import models as auth_models
from djkatta.accounts.models import hash_len


class RoomManager(models.Manager):
    def get_queryset(self):
        return super(RoomManager, self).get_queryset().filter(req_open='O')


class room_requirement(models.Model):
    """Model to save any room requirement details"""

    owner = models.ForeignKey(auth_models.User, on_delete=models.PROTECT)

    req_status_choices = (
        ('O', 'Open'),
        ('C', 'Closed'),
    )
    req_open = models.CharField(default="O", choices=req_status_choices,
                                max_length=2, help_text="Status of the request",
                                verbose_name="Request Status")

    contact_number = models.CharField(blank=True, max_length=16,
                                      help_text="Contact number (optional)")

    gender_req_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('A', 'Any'),
    )
    gender_req = models.CharField(default="A", choices=gender_req_choices,
                                  max_length=2, help_text="Gender requirement",
                                  verbose_name="Gender requirement")

    locality = models.CharField(max_length=64, help_text="Name of locality/society")
    rent = models.IntegerField(help_text="Rent per month (in Rs.)")
    deposit = models.IntegerField(help_text="Security deposit (in Rs.)")
    vacancies = models.IntegerField(default=1, help_text="Total vacancies (no. of persons)")
    office_dist = models.IntegerField(null=True, blank=True, help_text="Distance from ITPL office (in kms)")
    more_details = models.CharField(blank=True, max_length=2048, help_text="Additional details")

    added_on = models.DateTimeField(auto_now_add=True, help_text="Internal field")

    # default manager
    objects = models.Manager()
    # custom manager for filtering of "closed" & "old but open" posts
    active = RoomManager()

    def __unicode__(self):
        return "{0} - {1}".format(self.locality, self.owner.username)

    def get_post_url(self):
        return reverse('roomreq:indi', kwargs={'post_id':self.id})

    class Meta:
        verbose_name = "Room Requirement"
        ordering = ['added_on',]
