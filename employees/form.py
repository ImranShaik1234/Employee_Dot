from django import forms
from .models import Employees

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ('name', 'emp_ID', 'mobile_no', 'email', 'department')