from rest_framework import serializers
from .models import ServiceType, Booking, JobAssignment

class ServiceTypeSerializers(serializers.ModelSerializer):
  class Meta:
    model = ServiceType
    fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Booking
    fields = '__all__'

class JobAssignmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = JobAssignment
    fields = '__all__'