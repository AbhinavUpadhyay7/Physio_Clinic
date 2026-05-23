from django.urls import path
from .views import (
    doctor_login,
    dashboard,
    doctor_logout,
    approve_appointment,
    reject_appointment,
    delete_appointment,
    edit_appointment
)

from .views import (
    doctor_login,
    dashboard,
    doctor_logout
)

urlpatterns = [

    path('login/', doctor_login, name='login'),

    path('dashboard/', dashboard, name='dashboard'),

    path('logout/', doctor_logout, name='logout'),

    path(
    'approve/<int:id>/',
    approve_appointment,
    name='approve'
),

path(
    'reject/<int:id>/',
    reject_appointment,
    name='reject'
),


path(
    'delete/<int:id>/',
    delete_appointment,
    name='delete'
),
path(
    'edit/<int:id>/',
    edit_appointment,
    name='edit'
),
]