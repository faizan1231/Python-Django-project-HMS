from django.db import models

# Define the Doctor model
class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    special = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Define the Patient model
class Patient(models.Model):
    sname = models.CharField(max_length=50)
    gender = models.CharField(max_length=30)
    contact = models.CharField(max_length=50, null=True)  # Changed to CharField to match the length
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name

# Define the Appointment model
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    

    def __str__(self):
        return f"{self.doctor.name} -- {self.patient.name}"

