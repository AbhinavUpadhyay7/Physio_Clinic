from django.urls import path

from .views import (
    book_appointment,
    patient_records,
    dashboard,
    approve_appointment,
    reject_appointment,
    edit_appointment,
    delete_appointment,
)

urlpatterns = [

    path(
        'book/',
        book_appointment,
        name='book_appointment'
    ),

    path(
        'records/',
        patient_records,
        name='records'
    ),

    path(
        'dashboard/',
        dashboard,
        name='dashboard'
    ),

    path(
        'approve/<int:id>/',
        approve_appointment,
        name='approve_appointment'
    ),

    path(
        'reject/<int:id>/',
        reject_appointment,
        name='reject_appointment'
    ),

    path(
        'edit/<int:id>/',
        edit_appointment,
        name='edit_appointment'
    ),

    path(
        'delete/<int:id>/',
        delete_appointment,
        name='delete_appointment'
    ),
]