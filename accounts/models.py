from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    Role = (
        ('admin', 'مدیر'),
        ('patient', 'بیمار'),
        ('advisor', 'مشاور'),
    )
    role = models.CharField(max_length=10, choices=Role, default='patient')
    email = models.EmailField(max_length=150,unique=True)
    phone_number = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)

    def is_admin(self):
        return self.role == 'admin'
    def is_patient(self):
        return self.role == 'patient'
    def is_advisor(self):
        return self.role == 'advisor'

