from django.db import models
from .doctor import Doctor

class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.doctor.full_name} - {self.start_time} to {self.end_time}"
