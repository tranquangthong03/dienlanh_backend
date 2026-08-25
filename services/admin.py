from django.contrib import admin
from .models import ServiceType, Booking, JobAssignment

admin.site.register(ServiceType)
admin.site.register(Booking)
admin.site.register(JobAssignment)