from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Employee


def emp_list(request):
    employees = Employee.objects.all()
    return render(request, 'portal/list.html', {'employees': employees})
