from django.contrib import admin
from djkatta.cabshare.models import cab_sharing


class CabShareAdmin(admin.ModelAdmin):
    list_display = ('owner', 'destination', 'travel_date',)
    list_filter = ('travel_date', 'destination',)


admin.site.register(cab_sharing, CabShareAdmin)
