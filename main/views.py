from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Departments, Doctors

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_confirmation')

    form = BookingForm()
    return render(request, 'booking.html', {"form": form})

def booking_confirmation(request):
    return render(request, 'confirmation.html')

def doctors(request):
    return render(request, 'docters.html', {
        'doctors': Doctors.objects.select_related("dep_name").all()
    })

def department(request):
    return render(request, 'department.html', {
        'dept': Departments.objects.all()
    })

def contact(request):
    return render(request, 'contact.html')
