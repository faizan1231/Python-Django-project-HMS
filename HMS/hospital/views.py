from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout as auth_logout,login
from .models import *
from django.contrib import messages
from django import forms
from .form import DoctorForm,PatientForm,AppointmentForm  
# Create your views here.


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def navs(request):
    return render(request, 'navigationbar.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')  # Redirect to login page if not staff

    # Get all objects
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()

    # Count the number of each type
    d = doctors.count()
    p = patients.count()
    a = appointments.count()

    # Prepare context data
    context = {
        'd': d,
        'p': p,
        'a': a
    }

    return render(request, 'index.html', context)

def Login(request):
    error = ""
    d = {'error': error}  # Initialize `d` at the start

    if request.method == 'POST':
        u = request.POST.get('uname', '')  # Use .get() to avoid KeyError
        p = request.POST.get('pwd', '')    # Use .get() to avoid KeyError
        
        user = authenticate(username=u, password=p)
        
        if user is not None:
            if user.is_staff:
                login(request, user)
                error = "yes"
            else:
                error = "not"
        else:
            error = "not"
        
        d['error'] = error  # Update `d` with the current error message

    return render(request, 'login.html', d)

def logout(request):
    if not request.user.is_staff:
        return redirect('login')  # Redirect to login page if not staff
    
    auth_logout(request)  # Correctly call Django's logout function
    return redirect('login')


def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc =  Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'view_doctor.html',d)


def add_doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
            n = request.POST['name']
            c = request.POST['contact']
            sp = request.POST['special']
            try:
                Doctor.objects.create(name=n,mobile=c,special=sp)
                error="no"
           
            except:
               error = "yes"
    d = {'error':error}
    return render(request,'add_doctor.html',d)
    
def delete_doctor(request,pid):
       if not request.user.is_staff:
           return redirect('login')
       doctor = Doctor.objects.get(id=pid)
       doctor.delete()
       return redirect('view_doctor')

def edit_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated successfully.')
            return redirect('view_doctor')  # Adjust if you need to redirect to a different view
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = DoctorForm(instance=doctor)
    
    return render(request, 'edit_doctor.html', {'form': form, 'doctor': doctor})
    
def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat =  Patient.objects.all()
    t = {'pat':pat}
    return render(request,'view_patient.html',t)

def add_patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        sn = request.POST['sname']
        gn = request.POST['gender']
        cn = request.POST['contact']
        adr = request.POST['address']
        try:
            Patient.objects.create(sname=sn, gender=gn, contact=cn, address=adr)
            error = "no"
        except:
            error = "yes"
    a = {'error': error}
    return render(request, 'add_patient.html', a)


def delete_patient(request,pid):
       if not request.user.is_staff:
           return redirect('login')
       doctor = Patient.objects.get(id=pid)
       doctor.delete()
       return redirect('view_patient')    

def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Let you to Edit Page.')
            return redirect('view_patient')  # Adjust if you need to redirect to a different view
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        forms = PatientForm(instance=patient)
    
    return render(request, 'edit_patient.html', {'forms': forms, 'patient': patient})


def add_appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    doctor_list = Doctor.objects.all()
    patient_list = Patient.objects.all()

    if request.method == 'POST':
        d_name = request.POST.get('doctor')
        p_name = request.POST.get('patient')
        date = request.POST.get('date')

        try:
            # Fetch doctor and patient objects
            doctor = Doctor.objects.filter(name=d_name).first()
            patient = Patient.objects.filter(sname=p_name).first()
            
            if not doctor or not patient:
                raise ValueError("Invalid doctor or patient")

            # Create the appointment
            Appointment.objects.create(doctor=doctor, patient=patient, date=date)
            error = "no"
        except ValueError as ve:
            error = f"Error: {ve}"
        except Exception as e:
            error = f"An error occurred: {e}"

    context = {'doctor': doctor_list, 'patient': patient_list, 'error': error}
    return render(request, 'add_appointment.html', context)

def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')

    appointments = Appointment.objects.all()
    context = {'appoint': appointments}
    return render(request, 'view_appointment.html', context)

def delete_appointment(request, pid):
    if not request.user.is_staff:
        return redirect('login')

    try:
        appointment = Appointment.objects.get(id=pid)
        appointment.delete()
        return redirect('view_appointment')
    except Appointment.DoesNotExist:
        return redirect('view_appointment')  # Or render an error page/message
    

def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    doctors = Doctor.objects.all()  # Fetch all doctors
    patients = Patient.objects.all()  # Fetch all patients

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment updated successfully.')
            return redirect('view_appointment')  # Adjust the redirect URL as needed
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AppointmentForm(instance=appointment)
    
    return render(request, 'edit_appointment.html', {
        'form': form,
        'appointment': appointment,
        'doctors': doctors,
        'patients': patients,
        
    })