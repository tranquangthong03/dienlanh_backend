from rest_framework import viewsets
from .models import ServiceType, Booking, JobAssignment
from .serializers import ServiceTypeSerializers, BookingSerializer, JobAssignmentSerializer

# Create your views here.

class ServiceTypeViewSet(viewsets.ModelViewSet):
  queryset = ServiceType.objects.all()
  serializer_class = ServiceTypeSerializers

class BookingViewSet(viewsets.ModelViewSet):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer

class JobAssignmentViewSet(viewsets.ModelViewSet):
  queryset = JobAssignment.objects.all()
  serializer_class = JobAssignmentSerializer