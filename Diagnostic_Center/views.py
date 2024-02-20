from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from .models import *
from django.contrib.auth import authenticate, logout, login

# Create your views here.

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'index.html')

def Login(request):
    error=""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'login.html', d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')


def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'view_doctor.html', d)

def Add_Doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        sp = request.POST['specialization']
        try:
            Doctor.objects.create(name=n, mobile=c, specialization=sp)
            error="no"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'add_doctor.html', d)

def Delete_Doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')


def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d = {'pat': pat}
    return render(request, 'view_patient.html', d)

def Add_Patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
        a = request.POST['age']
        add = request.POST['address']
        try:
            Patient.objects.create(name=n, gender=g, mobile=m, age=a, address=add)
            error="no"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'add_patient.html', d)

def Delete_Patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')

def View_Technician(request):
    if not request.user.is_staff:
        return redirect('login')
    tec = Technician.objects.all()
    d = {'tec': tec}
    return render(request, 'view_technician.html', d)

def Add_Technician(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
        try:
            Technician.objects.create(name=n, gender=g, mobile=m)
            error="no"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'add_technician.html', d)

def Delete_Technician(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    technician = Technician.objects.get(id=pid)
    technician.delete()
    return redirect('view_technician.html')

def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    app = Appointment.objects.all()
    a = {'app': app}
    return render(request, 'view_appointment.html', a)

def Add_Appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    
    if request.method == 'POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        m = request.POST['mobile']
        d1 = request.POST['date']
        t = request.POST['time']
        
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor, patient=patient, mobile=m, date1=d1, time1=t)
            error="no"
        except:
            error="yes"
    l = {'doctor': doctor1, 'patient':patient1, 'error':error}
    return render(request, 'add_appointment.html', l)

def Delete_Appointment(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment.html')
    

    

    

