from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Employee
from .filters import EmployeeFilter

def emp_list(request):
    employees = Employee.objects.all()
    return render(request, 'portal/list.html', {'employees': employees})

def search(request):
    emp_list = Employee.objects.all()
    emp_filter = EmployeeFilter(request.GET, queryset=emp_list)
    return render(request, 'portal/search.html', {'filter': emp_filter})