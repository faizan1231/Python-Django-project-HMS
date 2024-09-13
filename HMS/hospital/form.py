# forms.py

from django import forms
from .models import Doctor, Patient,Appointment

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'mobile', 'special']  # Include the fields you want in the form

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['sname', 'gender', 'contact', 'address']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor','patient','date']
