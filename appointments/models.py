from django.db import models

class Appointments(models.Model):
    STATUS = (
        ('pending', 'در انتظار تایید'),
        ('canceled', 'کنسل شده'),
        ('available', 'در دسترس'),
        ('not_available', 'غیر قابل دسترس'),
        ('booked', 'رزرو شده'),
    )
    advisor = models.ForeignKey('accounts.User', on_delete=models.CASCADE, limit_choices_to={'role':'advisor'}, related_name='advisor')
    appointment_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    patient = models.ForeignKey('accounts.User' , on_delete=models.SET_NULL, limit_choices_to={'role':'patient'}, related_name='patient', blank=True, null=True)

    def get_advisor_full_name(self):
        return f"{self.advisor.first_name} {self.advisor.last_name}"

    def __str__(self):
        return f"{self.get_advisor_full_name()} - {self.appointment_time}"
