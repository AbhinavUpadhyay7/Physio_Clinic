from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from datetime import date

from .forms import AppointmentForm
from .models import Appointment


# =========================================
# BOOK APPOINTMENT
# =========================================

def book_appointment(request):

    if request.method == 'POST':

        form = AppointmentForm(request.POST)

        print(form.errors)

        if form.is_valid():

            # SAVE APPOINTMENT

            appointment = form.save()

            # =================================
            # EMAIL TO PATIENT
            # =================================

            send_mail(

                'Appointment Confirmation',

                f'''
Hello {appointment.patient_name},

Your appointment has been booked successfully.

Appointment Details:

Date:
{appointment.appointment_date}

Time:
{appointment.appointment_time}

Thank you for choosing
Physiotherapy Health Care Center
Dr. Vishal Upadhyay
Naini Prayagraj
''',

                None,

                [appointment.email],

                fail_silently=False,
            )

            # =================================
            # EMAIL TO DOCTOR
            # =================================

            send_mail(

                'New Appointment Booked',

                f'''
A new appointment has been booked.

Patient Details:

Name:
{appointment.patient_name}

Phone:
{appointment.phone}

Email:
{appointment.email}

Age:
{appointment.age}

Gender:
{appointment.gender}

Problem / Disease:
{appointment.problem}

Appointment Date:
{appointment.appointment_date}

Appointment Time:
{appointment.appointment_time}
''',

                None,

                ['vishal.physio786@gmail.com'],

                fail_silently=False,
            )

            # SUCCESS MESSAGE

            messages.success(

                request,

                'Appointment booked successfully! Check your Email.'

            )

            return redirect('/')

    else:

        form = AppointmentForm()

    return render(

        request,

        'appointment.html',

        {

            'form': form

        }
    )


# =========================================
# PATIENT RECORDS
# =========================================

def patient_records(request):

    appointments = Appointment.objects.all().order_by('-id')

    return render(

        request,

        'records.html',

        {

            'appointments': appointments

        }
    )


# =========================================
# DOCTOR DASHBOARD
# =========================================

def dashboard(request):

    appointments = Appointment.objects.all().order_by('-id')

    # =================================
    # COUNTS
    # =================================

    total_appointments = appointments.count()

    today_appointments = appointments.filter(

        appointment_date=date.today()

    ).count()

    pending_appointments = appointments.filter(

        status__iexact='Pending'

    ).count()

    approved_appointments = appointments.filter(

        status__iexact='Approved'

    ).count()

    rejected_appointments = appointments.filter(

        status__iexact='Rejected'

    ).count()

    updated_appointments = appointments.filter(

        status__iexact='Updated'

    ).count()

    return render(

        request,

        'dashboard.html',

        {

            'appointments': appointments,

            'total_appointments': total_appointments,

            'today_appointments': today_appointments,

            'pending_appointments': pending_appointments,

            'approved_appointments': approved_appointments,

            'rejected_appointments': rejected_appointments,

            'updated_appointments': updated_appointments,

        }
    )


# =========================================
# APPROVE APPOINTMENT
# =========================================

def approve_appointment(request, id):

    appointment = Appointment.objects.get(id=id)

    appointment.status = 'Approved'

    appointment.save()

    # EMAIL TO PATIENT

    send_mail(

        'Appointment Approved',

        f'''
Hello {appointment.patient_name},

Your appointment has been APPROVED.

Appointment Details:

Date:
{appointment.appointment_date}

Time:
{appointment.appointment_time}

Please arrive 10 minutes before appointment.

Regards,
Physiotherapy Health Care Center
Dr. Vishal Upadhyay
''',

        None,

        [appointment.email],

        fail_silently=False,
    )

    return redirect('/appointments/dashboard/')


# =========================================
# REJECT APPOINTMENT
# =========================================

def reject_appointment(request, id):

    appointment = Appointment.objects.get(id=id)

    reason = request.GET.get('reason')

    appointment.status = 'Rejected'

    appointment.reason = reason

    appointment.save()

    # EMAIL TO PATIENT

    send_mail(

        'Appointment Rejected',

        f'''
Hello {appointment.patient_name},

We regret to inform you that your appointment has been rejected.

Reason:
{reason}

Please book another slot or contact clinic support.

Regards,
Physiotherapy Health Care Center
Dr. Vishal Upadhyay
''',

        None,

        [appointment.email],

        fail_silently=False,
    )

    return redirect('/appointments/dashboard/')


# =========================================
# EDIT APPOINTMENT
# =========================================

def edit_appointment(request, id):

    appointment = Appointment.objects.get(id=id)

    if request.method == 'POST':

        form = AppointmentForm(

            request.POST,

            instance=appointment
        )

        if form.is_valid():

            updated_appointment = form.save(
                commit=False
            )

            updated_appointment.status = 'Updated'

            updated_appointment.save()

            # EMAIL TO PATIENT

            send_mail(

                'Appointment Updated',

                f'''
Hello {updated_appointment.patient_name},

Your appointment has been UPDATED by doctor.

Updated Appointment Details:

Date:
{updated_appointment.appointment_date}

Time:
{updated_appointment.appointment_time}

Please check updated schedule carefully.

Regards,
Physiotherapy Health Care Center
Dr. Vishal Upadhyay
''',

                None,

                [updated_appointment.email],

                fail_silently=False,
            )

            return redirect('/appointments/dashboard/')

    else:

        form = AppointmentForm(
            instance=appointment
        )

    return render(

        request,

        'edit_appointment.html',

        {

            'form': form

        }
    )


# =========================================
# DELETE APPOINTMENT
# =========================================

def delete_appointment(request, id):

    appointment = Appointment.objects.get(id=id)

    appointment.delete()

    return redirect('/appointments/dashboard/')