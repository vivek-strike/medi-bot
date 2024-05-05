
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from main.views import deletehospital, AddHospital,HomeView, Diabetes, Heart, Breast, consultation, appointment, signup, registration, signout, admin_view, add_doctor, consultation_request, consultation_delete, doctor_list,RedirectError, Index
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",Index,name="Index"),
    path('signup',signup,name='signup'),
    path('registration',registration,name='registration'),
    path('signout',signout,name='signout'),
    path('admin_view',admin_view,name='admin_view'),
    path("home",HomeView,name="home"),
    path("Diabetes",Diabetes,name="diabetes"),
    path("Heart",Heart,name="heart"),
    path("Breast",Breast,name="breast"),
    path('consultation',consultation,name='consultation'),
    path('appointment',appointment,name='appointment'),
    path('add_doctor',add_doctor,name='add_doctor'),
    path('consultation_request',consultation_request,name='consultation_request'),
    path('consultation_delete',consultation_delete,name='consultation_delete'),
    path('doctor_list',doctor_list,name='doctor_list'),
    path("RedirectError",RedirectError,name="RedirectError"),
    path("AddHospital",AddHospital,name="AddHospital"),
    path("deletehospital/<int:pk>",deletehospital,name="deletehospital"),
    path("ViewHospital",views.ViewHospital,name="ViewHospital"),
    path("deletedoctor/<int:pk>",views.deletedoctor,name="deletedoctor"),
    path("GetAppointment/<int:pk>",views.GetAppointment,name="GetAppointment"),
    path("consultation_request_admin",views.consultation_request_admin,name="consultation_request_admin"),
    path("MedReminder",views.MedReminder,name="MedReminder"),



    
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
