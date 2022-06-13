from django.shortcuts import render
from django.shortcuts import render, redirect
from sympy import Integer

from Admin.models import Department, Patient,ticket
from .forms import Feedform, PatientForm, ticketForm
# Home Page


def home(request):
    clincs = Department.objects.all()
    return render(request, "Home/home.html",{'clincs':clincs})


def children(request):
    return render(request, "clinic/children.html")


def digestion(request):
    return render(request, "clinic/digestion.html")


def ear(request):
    return render(request, "clinic/ear.html")


def eyes(request):
    return render(request, "clinic/eyes.html")


def gyn(request):
    return render(request, "clinic/gyn.html")


def heart(request):
    return render(request, "clinic/heart.html")


def internal(request):
    return render(request, "clinic/internal.html")


def kidney(request):
    return render(request, "clinic/kidney.html")


def oncology(request):
    return render(request, "clinic/oncology.html")


def radiology(request):
    return render(request, "clinic/radiology.html")


def teeth(request):
    return render(request, "clinic/teeth.html")


def urology(request):
    return render(request, "clinic/urology.html")


def profile(request):
    return render(request, 'Profile/profile.html')


def reserve(request,id):
    form = PatientForm(request.POST or None, request.FILES or None)
    data = Department.objects.get(pk=id).id
    if form.is_valid():
        return redirect('ticket')
    return render(request, 'reservation/reserv.html', {'form': form,'data':data})


def Ticket(request,id):
    depid = Department.objects.get(pk=id);
    
    form = PatientForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        name = cd['Name']
        form.save()
        patient = Patient.objects.filter(National_num=cd['National_num']).first()
        saveticket = ticket.objects.create(Pat=patient,dept=depid,startdate=request.POST.get('start'))
    return render(request, "Ticket/ticket.html", {'name': name,'depts':depid,'code':saveticket.id,'start':saveticket.startdate})


def more_serv(request):
    clincs = Department.objects.all()
    
    return render(request, 'MoreServ/moreServ.html',{'clincs':clincs})


def arabic(request):
    return render(request, "Arabic/arabic.html")


def ARsingup(request):
    return render(request, "LOGIN/arabic/index2.html")


def ARlogin(request):
    return render(request, "LOGIN/arabic/index.html")


def forgetEmail(request):
    return render(request, 'forget/forget.html')




def showclinc(request,id):
    clinc = Department.objects.get(pk=id)
    rate = clinc.rate
    return render(request,'clinic/clinc.html',{'clinc':clinc,'range':range(0,rate)})

def add_Feedback(request):
    form = Feedform()
    if request.method == 'POST':

        form = Feedform(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('Home')
