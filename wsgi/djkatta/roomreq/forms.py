from django import forms
from djkatta.roomreq.models import room_requirement


class RoomReqForm(forms.ModelForm):
    class Meta:
        model = room_requirement
        exclude = ('id', 'owner', 'modified_on',)
