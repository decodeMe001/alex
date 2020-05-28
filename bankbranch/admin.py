from django.contrib import admin
from django.contrib.auth.models import Group
from . models import BankBranch

"""" Creating a custom Admin"""
class BankBranchAdmin(admin.ModelAdmin):
    list_display = ('bank', 'state', 'location', 'address', 'email')
    list_filter = ('bank', 'state', 'location')
    search_fields = ('bank', 'state', 'location')

admin.site.register(BankBranch, BankBranchAdmin)
admin.site.unregister(Group)
