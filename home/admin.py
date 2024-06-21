from django.contrib import admin
from . import models

admin.site.register(models.Department)
admin.site.register(models.Doctor)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','pat_name','pat_email','pat_phone','doc_name','booking_date','booked_on')

admin.site.register(models.Booking,BookingAdmin)
