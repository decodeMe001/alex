from django.contrib import admin
from .models import Choice, Poll, Opinion

# Register your models here.
admin.site.register(Choice)
admin.site.register(Poll)
admin.site.register(Opinion)
