from django.db import models
from django.utils import timezone

# Create your models here.
class Appointment(models.Model):
    SHIFT_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
        ('night', 'Night'),
    ]
    patient_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, default='0000000000')
    shift = models.CharField(
        max_length=20, 
        choices=SHIFT_CHOICES,
        default='morning'  # Default shift
    )
    location = models.CharField(max_length=100, default='Ellenabad')
    created_at = models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.patient_name