from django.shortcuts import render
from django.http import HttpResponse
from .models import Department


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'booking.html')

def doctors(request):
    return render(request, 'doctors.html')

def contact(request):
    return render(request, 'contact.html')

def department(request):
    dept_dic = {
        'depts' : Department.objects.all()
    }
    return render(request, 'department.html', dept_dic)