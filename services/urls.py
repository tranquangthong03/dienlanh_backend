from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceTypeViewSet, BookingViewSet, JobAssignmentViewSet

router = DefaultRouter()
router.register(r'service-types', ServiceTypeViewSet)
router.register(r'bookings', BookingViewSet)
router.register(f'job-assignment', JobAssignmentViewSet)

urlpatterns = [
  path('', include(router.urls))
]