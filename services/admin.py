from django.contrib import admin
from .models import Category, Product, ServiceType, Booking, JobAssignment

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ServiceType)
admin.site.register(Booking)
admin.site.register(JobAssignment)