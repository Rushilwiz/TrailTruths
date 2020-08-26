from django.contrib import admin
from .models import Poll, Answer, Location

# Register your models here.

admin.site.register(Location)
admin.site.register(Poll)
admin.site.register(Answer)