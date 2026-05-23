from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:

        model = Appointment

        exclude = ['status', 'reason']

        widgets = {

            'patient_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Patient Name'
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Mobile Number'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Email Address'
                }
            ),

            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Age'
                }
            ),

            'gender': forms.Select(
                attrs={
                    'class': 'form-control'
                },
                choices=[
                    ('Male', 'Male'),
                    ('Female', 'Female'),
                    ('Other', 'Other')
                ]
            ),

            'problem': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Describe Your Problem',
                    'rows': 4
                }
            ),

            'appointment_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            # IMPORTANT FIX

            'appointment_time': forms.TimeInput(

                attrs={

                    'type': 'time',

                    'class': 'form-control'
                }
            ),
        }