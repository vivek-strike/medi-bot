from django.db import models
from django.contrib.auth.models import User

# Create your models here.


    



class Hospital(models.Model):
    Hosptal_name = models.CharField(max_length=255)
    Image = models.FileField(upload_to="hospitel_image")
    Area = models.CharField(max_length=20)
    City = models.CharField(max_length=20)
    Country = models.CharField(max_length=26)
    Symptoms = models.CharField(max_length=1000)
    phone = models.IntegerField()

    def __str__(self):
        return str(self.Hosptal_name)


class DoctorAdd(models.Model):
    
    Doctor_name = models.CharField(max_length=200)
    Doctor_spacial = models.CharField(max_length=200)
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.Doctor_name)


class Doctor_consultation(models.Model):

    Patiant_name = models.CharField(max_length=200)
    Patiant_disease = models.CharField(max_length=200, null=True, blank=True)
    Doctor_name = models.ForeignKey(DoctorAdd, on_delete=models.CASCADE,null=True)
    hospital = models.ForeignKey(Hospital,models.CASCADE,null=True)
    appoiment_time = models.TimeField(auto_now_add=False)
    appointment_date = models.DateField(auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    
