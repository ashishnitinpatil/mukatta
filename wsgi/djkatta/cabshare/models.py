from django.db import models
from django.contrib.auth import models as auth_models
from django.core.urlresolvers import reverse


class CabManager(models.Manager):
    def get_queryset(self):
        return super(CabManager, self).get_queryset().filter(req_open='O')


class cab_sharing(models.Model):
    """Model to save any cab sharing details"""

    owner = models.ForeignKey(auth_models.User, on_delete=models.PROTECT)
    req_status_choices = (
        ('O', 'Open'),
        ('C', 'Closed'),
    )
    req_open = models.CharField(default=True, choices=req_status_choices,
                                max_length=2, help_text="Status of the request",
                                verbose_name="Request Status")

    contact_number = models.CharField(blank=True, max_length=16,
                                      help_text="Contact number (optional)")
    travel_date = models.DateField(null=True, help_text="Date on which cab is required")
    travel_time = models.TimeField(null=True, help_text="Time when cab is required")
    destination = models.CharField(default="Airport", max_length=64)
    already_booked = models.BooleanField(default=False, help_text="Already booked a cab?")

    pickup_from = models.CharField(blank=True, max_length=128, help_text="Pickup location")
    estimated_cost = models.IntegerField(null=True, blank=True,
                                         help_text="Estimated total cost of the trip by cab")
    cab_company = models.CharField(blank=True, help_text="Name of the cab company",
                                   max_length=64)
    cab_type    = models.CharField(blank=True, help_text="Type of the cab (mini, sedan, rickshaw)",
                                   max_length=32)
    passengers  = models.IntegerField(blank=True, null=True, help_text="Number of accompanying passengers")

    # default manager
    objects = models.Manager()
    # custom manager to account for default filtering of closed posts
    active = CabManager()

    def __unicode__(self):
        return "{0} - {1}".format(self.destination, self.owner.username)

    def get_post_url(self):
        return reverse('cabshare:indi', kwargs={'post_id':self.id})

    def save(self, *args, **kwargs):
        if not self.already_booked:
            self.pickup_from = ""
            self.estimated_cost = None
            self.cab_company = ""
            self.cab_type = ""
            self.passengers = None
        super(cab_sharing, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Cab Sharing"
        ordering = ['travel_date', 'travel_time']
