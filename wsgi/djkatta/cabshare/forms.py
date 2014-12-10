from django.forms import ModelForm
from djkatta.cabshare.models import cab_sharing


class CabShareForm(ModelForm):
    class Meta:
        model = cab_sharing
        exclude = ('id', 'owner',)
