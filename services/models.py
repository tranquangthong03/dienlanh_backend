from django.conf import settings
from django.db import models


class ServiceType(models.Model):
  name = models.CharField(max_length=100, verbose_name="Tên dịch vụ")
  base_price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Giá cơ bản (VND)")
  estimated_time = models.PositiveIntegerField(help_text="Thời gian dự kiến thi công (phút)", default=60)
  def __str__(self):
    return self.name

class Booking(models.Model):
  STATUS_CHOICES = (
    ('PENDING', 'Chờ xác nhận'),
    ('CONFIRMED', 'Đã xác nhận'),
    ('IN_PROGRESS', 'Đang thực hiện'),
    ('COMPLETED', 'Đã hoàn thành'),
    ('CANCELLED', 'Đã hủy'),
  )
  customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings', verbose_name="Khách hàng")
  service = models.ForeignKey(ServiceType, on_delete=models.CASCADE, verbose_name="Dịch vụ")
    
  scheduled_datetime = models.DateTimeField(verbose_name="Thời gian hẹn")
  address = models.TextField(verbose_name="Địa chỉ thi công")
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING', verbose_name="Trạng thái")
  created_at = models.DateTimeField(auto_now_add=True)
  notes = models.TextField(blank=True, null=True, verbose_name="Ghi chú của khách")

  def __str__(self):
    return f"{self.customer.username} - {self.service.name} ({self.get_status_display()})"

class JobAssignment(models.Model):
  booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='assignment')
  technician = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='jobs', verbose_name="Thợ phụ trách")
  assigned_at = models.DateTimeField(auto_now_add=True)
  completion_notes = models.TextField(blank=True, null=True, verbose_name="Ghi chú sau khi hoàn thành")

  def __str__(self):
    return f"Công việc: {self.booking.id} - Thợ: {self.technician.username}"