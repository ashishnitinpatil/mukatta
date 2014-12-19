from django.contrib import admin
from djkatta.roomreq.models import room_requirement


class RoomReqAdmin(admin.ModelAdmin):
    list_display = ('owner', 'locality', 'gender_req',)
    list_filter = ('locality', 'gender_req',)


admin.site.register(room_requirement, RoomReqAdmin)
