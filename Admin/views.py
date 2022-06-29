from datetime import datetime
import os
from django.shortcuts import redirect, render
from django.contrib import messages
from Admin.forms import clincform, doctorform, patientform, ticketform
from Admin.models import Department, Patient, Doctor, ticket,feedback
from Project.forms import PatientForm

# Create your views here.


def Dashboard(request):
    firstfeed =feedback.objects.first()
    lastfeed =feedback.objects.last()
    
    list_of_price =[]
    price = ticket.objects.all() 
    for i in price:
        list_of_price.append(i.dept.price)
    res =  sum(list_of_price)
    Departmentcount = Department.objects.count()
    patientscount = Patient.objects.count()
    doctorscount = Doctor.objects.count()
    ticketcount = ticket.objects.count()
    return render(request, 'Dashbord.html', {'lastfed':lastfeed,'fed':firstfeed,'total':res,'deps': Departmentcount, 'pat': patientscount, 'doc': doctorscount, 'ticket': ticketcount})


def Feedback(request):
    feeds = feedback.objects.all()
    return render(request, 'feedback.html',{'feeds':feeds})


def department(request):
    deps = Department.objects.all()

    form = clincform(request.POST or None, request.FILES or None)
    context = {'deps': deps, 'form': form}
    if form.is_valid():
        form.save()
        messages.success(request, "A Clincal Has Been Added Succesfully ")
        return redirect('Dashboard/departments')
    return render(request, 'departments.html', context)


def doctor(request):
    docs = Doctor.objects.all()
    form = doctorform(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Succesfully added")
        return redirect('Dashboard/doctors')
    context = {'docs': docs, 'form': form}
    return render(request, 'doctors.html', context)

def patients(request):
    patients = Patient.objects.all()  
    form = patientform(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Succesfully added")
        # return redirect('Dashboard/patients')
    context = {'patients': patients, 'form': form}
    return render(request, 'patients.html', context)


def Ticket(request):
    tics= ticket.objects.all()
    form = ticketform(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Ticket Succesfully added")
    return render(request,'ticket.html',{'tics':tics,'form':form})


# Dashboard action
def deletedepartment(request, depid):
    dep = Department.objects.get(pk=depid)
    if len(dep.img) > 0:
        os.remove(dep.img.path)
    dep.delete()
    messages.success(request, "A Clincal Has Been Deleted Succesfully ")
    return redirect('Dashboard/departments')


def searchdepartment(request):
    # item = Items()
    if request.method == "POST":
        key = request.POST.get('search')
        form = clincform(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "A Clincal Has Been Added Succesfully ")
        res = Department.objects.filter(name__icontains=key)
        return render(request, "search_dep.html", {"departments": res, 'form': form})
    else:
        return render(request, "search_dep.html", {})


def editdepartment(request, id):
    data = Department.objects.get(pk=id)
    form = clincform(instance=data)
    context = {'data': data,'form':form}
    return render(request, 'edit_department.html', context)

def updatedepartment(request,id):
    data = Department.objects.get(pk=id)
    form = clincform()
    if request.method == "POST":
        form = clincform(request.POST or None, request.FILES or None,instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Clical Updated Succesfuly')
            return redirect("Dashboard/departments")
        else:
            return redirect('edit_department',data.id)


def deletepatient(request, p_id):
    item = Patient.objects.get(id=p_id)
    item.delete()
    messages.success(request, "A Patient Has Been Deleted Succesfully ")

    return redirect('Dashboard/patient')


def searchpatient(request):
    form = patientform(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Succesfully added")
    if request.method == 'POST':
        key = request.POST.get('search')
        
        res = Patient.objects.filter(Name__icontains=key)

        return render(request, "searchpatient.html", {"patients": res,'form':form})
    else:
        return render(request, "searchpatient.html", {})

def editpatient(request,id):
    data = Patient.objects.get(pk=id)
    form = patientform(instance=data)
    context = {'data': data,'form':form}
    return render(request, 'edit_patient.html', context)

def updatepatient(request,id):
    data = Patient.objects.get(pk=id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "A Patient Has Been Updated Succesfully ")
            return redirect('Dashboard/patient')
        else:
            # messages.success(request, "A Patient Has Been Updated Succesfully ")
            return redirect('editpatient',data.id)

def searchticket(request):
    
    if request.method == 'POST':
        form = ticketform(request.POST or None, request.FILES or None)
        key = request.POST.get('search')
        res = ticket.objects.filter(Pat__Name__contains = key)
        return render(request, "searchticket.html", {"ticket": res,'form':form})
    else:
        return render(request, "searchticket.html", {})

def deletedoctor(request, d_id):
    item = Doctor.objects.get(id=d_id)
    item.delete()
    messages.success(request, "A Doctor Has Been Deleted Succesfully ")
    return redirect('Dashboard/doctors')

def searchdoctor(request):
    
    if request.method == 'POST':
        form = doctorform(request.POST or None, request.FILES or None)
        key = request.POST.get('search')
        res = Doctor.objects.filter(name__icontains=key)
        return render(request, "searchdoctors.html", {"docs": res,'form':form})
    else:
        return render(request, "searchdoctors.html", {})

def editdoctor(request,id):
    data = Doctor.objects.get(pk=id)
    form = doctorform(instance=data)
    context = {'data': data,'form':form}
    return render(request, 'editdoctor.html', context)



def updatedoctor(request,id):
    data = Doctor.objects.get(pk=id)
    if request.method == 'POST':
        form = doctorform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "A Doctor Has Been Updated Succesfully ")
            return redirect('Dashboard/doctors')
        else:
            # messages.success(request, "A Patient Has Been Updated Succesfully ")
            return redirect('editdoctor',data.id)

def viewticket(request,id):
    data = ticket.objects.get(pk=id)
    return render(request,'view_ticket.html',{'ticket':data})

from django.db.models import Sum


def sumticket(request):
    
    list_of_price =[]
    price = ticket.objects.all() 
    for i in price:
        list_of_price.append(i.dept.price)
    res =  sum(list_of_price)
    return render(request,'base.html',{'total':res})