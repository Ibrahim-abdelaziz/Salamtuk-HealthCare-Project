from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from datetime import datetime


class Doctor(models.Model):
    Name         = models.CharField(null=False, blank=False, max_length=50)
    Title        = models.CharField(max_length=250, null=False,blank=False, default='')
    Iamge        = models.ImageField(upload_to='', null=True)
    Describtion  = models.CharField(null=False, blank=False, max_length=250)
    Specialized  = models.CharField(default="(select to)", choices=[
        ('Dermatologist', 'Dermatologist'),
        ('Neurologist', 'Neurologist'),
        ('Psychiatrist', 'Psychiatrist'),
        ('Bones', 'Bones'),
        ('Dentist', 'Dentist'),
        ('Cardiologist', 'Neurologist'),

    ], null=False, blank=False, max_length=50)
    Country        = CountryField(blank_label="(Select_country)", blank=True, null=True)
    Clinic_Address = models.CharField(null=False, blank=False, max_length=250)
    Clinic_Phone   = PhoneNumberField(null=False, blank=False)
    Check_Value    = models.CharField(null=False, blank=False, max_length=50)
    Period_of_wait = models.CharField(null=False, blank=False, max_length=50)

    def __str__(self):
        return self.Name

class Appoientment(models.Model):
    name_of_doctor   = models.ForeignKey(Doctor, related_name="Doctor", on_delete=models.CASCADE, null=False, blank=False)
    appoientment_day = models.CharField(default="(select to)", choices=[
        ('saturday', 'saturday'),
        ('sunday', 'sunday'),
        ('monday', 'monday'),
        ('tuseday', 'tuseday'),
        ('wensday', 'wensday'),
        ('thursday', 'thursday'),
        ('friday', 'friday'),], null=False, blank=False, max_length=250)
    appoientment_time = models.CharField(max_length=250, default="From:   To:  ")

    def __str__(self):
        return str(self.appoientment_day + self.appoientment_time)

class Paitent(models.Model):
    Name          = models.CharField(max_length=50)
    Age           = models.IntegerField()
    Birth_of_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.Name

class Booking(models.Model):
    doctor_id       = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor', null=False, blank=False, default="")
    Patient_id      = models.ForeignKey(Paitent,on_delete=models.CASCADE,related_name='paitent', null=False, blank=False, default="")
    Appoientment_id = models.ForeignKey(Appoientment,on_delete=models.CASCADE, related_name='Appoientment', null=False, blank=False, default="")

    def __str__(self):
        return self.Appoientment_id

class Comments(models.Model):
    comments    = models.CharField(max_length=250)
    Paitent     = models.ForeignKey(Paitent, related_name="Comments", on_delete=models.CASCADE, default="")
    Doctor      = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='Doctors')

class Attendance(models.Model):
    id_patient  = models.ForeignKey(Paitent, related_name="Attendance", on_delete=models.CASCADE, default="")
    is_Booking  = models.ForeignKey(Booking, related_name="Booking", on_delete=models.CASCADE, default="")
    is_attend   = models.BooleanField()

    def __str__(self):
        return self.Name

class Payment(models.Model):
    id_patient  = models.ForeignKey(Paitent, related_name="Payment", on_delete=models.CASCADE, default="")
    payment     = models.CharField(max_length=250, choices=[
        ('cash', 'Cash'),
        ('Visa', 'Visa'), ],)




