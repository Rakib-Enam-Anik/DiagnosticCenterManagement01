from django.contrib import admin
from django.urls import path

from Diagnostic_Center.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('', Index, name='home'),
    path('admin_login/', Login, name='login'),
    path('logout/', Logout_admin, name='logout'),
    path('view_doctor/', View_Doctor, name='view_doctor'),
    path('add_doctor/', Add_Doctor, name='add_doctor'),
    path('delete_doctor(?P<int:pid>)', Delete_Doctor, name='delete_doctor'),
    path('view_patient/', View_Patient, name='view_patient'),
    path('add_patient/', Add_Patient, name='add_patient'),
    path('delete_patient(?P<int:pid>)', Delete_Patient, name='delete_patient'),
    path('view_technician/', View_Technician, name='view_technician'),
    path('add_technician/', Add_Technician, name='add_technician'),
    path('delete_technician(?P<int:pid>)', Delete_Technician, name='delete_technician'),
    path('view_appointment/', View_Appointment, name='view_appointment'),
    path('add_appointment/', Add_Appointment, name='add_appointment'),
    path('delete_appointment(?P<int:pid>)', Delete_Appointment, name='delete_appointment'),
    
    
    
    
]
