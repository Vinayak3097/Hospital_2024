from django.shortcuts import render
from django.http import HttpResponse
from .models import Department,Doctor
from .forms import BookingForm


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request, 'booking.html', dict_form)

def doctors(request):
    doctor = {
        'docs' : Doctor.objects.all()
    }
    return render(request, 'doctors.html', doctor)

def contact(request):
    return render(request, 'contact.html')

def department(request):
    dept_dic = {
        'depts' : Department.objects.all()
    }
    return render(request, 'department.html', dept_dic)