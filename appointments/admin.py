from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        'patient_name',
        'phone',
        'appointment_date',
        'appointment_time',
        'status',
    )

    list_filter = ('status',)

    search_fields = (
        'patient_name',
        'phone',
    )