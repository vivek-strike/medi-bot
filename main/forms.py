from django.forms import fields, forms, ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DoctorAdd, Doctor_consultation

class UserRegistration(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']


class DoctorAddForm(ModelForm):
    class Meta:
        model = DoctorAdd
        fields = "__all__"


class ConsultationaddForm(ModelForm):
    class Meta:
        model = Doctor_consultation
        fields = ["Patiant_name","appoiment_time","appointment_date"]

        widgets = {
            "Patiant_name":TextInput(attrs={"class":"form-control"}),
            "appoiment_time":TextInput(attrs={"class":"form-control","type":"time"}),
            "appointment_date":TextInput(attrs={"class":"form-control","type":"date"}),
        }