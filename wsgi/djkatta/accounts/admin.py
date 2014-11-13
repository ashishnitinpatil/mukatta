from django.contrib import admin
from djkatta.accounts.models import pass_reset_validb


class PassResetValidbAdmin(admin.ModelAdmin):
    list_display = ('username', 'valid_hash', 'valid_upto')

admin.site.register(pass_reset_validb, PassResetValidbAdmin)
