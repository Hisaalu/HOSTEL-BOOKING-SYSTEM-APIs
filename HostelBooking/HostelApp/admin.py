from django.contrib import admin
from HostelApp.models import Room
from HostelApp.models import Hostel
from HostelApp.models import Booking


# Register your models here!.

admin.site.register(Room)
admin.site.register(Hostel)
admin.site.register(Booking)
