from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employees
from .form import EmployeeForm

def employee_list(request):
    employees = Employees.objects.all()
    return render(request, 'List_Employees.html', {'employees': employees})

def employee_new(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'register.html', {'form': form})

def employee_edit(request, pk):
    employee = get_object_or_404(Employees, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            messages.success(request, 'Employee details updated successfully')
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_edit.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employees, pk=pk)
    employee.delete()
    return redirect('employee_list')
