from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  # Định nghĩa các roles
  ROLE_CHOICES = (
    ('CUSTOMER', 'Khách hàng'),
    ('TECHNICIAN', 'Thợ kỹ thuật'),
    ('ADMIN', 'Quản trị viên'),
  )
  # Bổ sung các trường cần thiết
  role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='CUSTOMER')
  phone_number = models.CharField(max_length=15, blank=True, null=True)
  address = models.TextField(blank=True, null=True)

  def __str__(self):
    return f"{self.username} ({self.get_role_display()})"

class TechnicianProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='technician_profile')
  skills = models.CharField(max_length=255, help_text="VD: Máy lạnh, Tủ lạnh, Máy giặt")
  rating = models.FloatField(default=0.0)
  is_active = models.BooleanField(default=True, help_text="Thợ có đang đi làm không?")
  def __str__(self):
    return f"Profile thợ: {self.user.full_name}"