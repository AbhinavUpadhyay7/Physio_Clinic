from django.db import models

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    problem = models.TextField()

    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(
    max_length=20,
    default='Pending'
                   )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name
    
    reason = models.TextField(
    blank=True,
    null=True
)