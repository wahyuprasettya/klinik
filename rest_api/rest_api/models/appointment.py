from django.db import models
from .doctor import Doctor
from .patient import Patient

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')])
    reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Appointment for {self.patient} with {self.doctor} on {self.appointment_date}"