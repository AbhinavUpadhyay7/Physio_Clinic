# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from appointments.models import Appointment
from appointments.forms import AppointmentForm
from django.contrib import messages

from appointments.models import Appointment
from datetime import date


def doctor_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/dashboard/')
        else:

            messages.error(
                request,
                'Wrong username or password!'
            )

    return render(request, 'login.html')


@login_required
def dashboard(request):

    appointments = Appointment.objects.all().order_by('-created_at')

    total_appointments = appointments.count()

    today_appointments = Appointment.objects.filter(
        appointment_date=date.today()
    ).count()
    pending_appointments = Appointment.objects.filter(
    status='Pending').count()

    context = {

    'appointments': appointments,

    'total_appointments': total_appointments,

    'today_appointments': today_appointments,

    'pending_appointments': pending_appointments,
}

    return render(request, 'dashboard.html', context)


def doctor_logout(request):

    logout(request)

    return redirect('/')


# new
@login_required
def approve_appointment(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id
    )

    appointment.status = 'Approved'

    appointment.save()

    return redirect('/dashboard/')


@login_required
def reject_appointment(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id
    )

    appointment.status = 'Rejected'

    appointment.save()

    return redirect('/dashboard/')

@login_required
def delete_appointment(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id
    )

    appointment.delete()

    return redirect('/dashboard/')


@login_required
def edit_appointment(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id
    )

    form = AppointmentForm(
        request.POST or None,
        instance=appointment
    )

    if form.is_valid():

        form.save()

        return redirect('/dashboard/')

    return render(
        request,
        'edit_appointment.html',
        {'form': form}
    )