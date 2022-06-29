"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from Admin.models import feedback

from Admin.views import Dashboard, Feedback, Ticket, deletedepartment, deletedoctor, deletepatient, department, doctor, editdepartment, editdoctor, editpatient, patients, searchdepartment, searchdoctor, searchpatient, searchticket, sumticket, updatedepartment, updatedoctor, updatepatient, viewticket

from . import views
from Project.views import add_Feedback, children, digestion, ear, eyes, gyn, heart, internal, kidney, oncology, radiology, showclinc, teeth, urology, reserve, forgetEmail
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Dashboard', Dashboard, name='Dashboard'),
    path('Dashboard/patient', patients, name='Dashboard/patient'),
    path('Dashboard/feedback', Feedback, name='Dashboard/feedback'),
    path('Dashboard/departments', department, name='Dashboard/departments'),
    path('Dashboard/doctors', doctor, name='Dashboard/doctors'),
    path('Dashboard/ticket', Ticket, name='Dashboard/ticket'),
    path('clinic/', children, name='children'),
    path('clinic1/', digestion, name='digestion'),
    path('clinic2/', ear, name='ear'),
    path('clinic3/', eyes, name='eyes'),
    path('clinic4/', gyn, name='gyn'),
    path('clinic5/', heart, name='heart'),
    path('clinic6/', internal, name='internal'),
    path('clinic7/', kidney, name='kidney'),
    path('clinic8/', oncology, name='oncology'),
    path('clinic9/', radiology, name='radiology'),
    path('clinic10/', teeth, name='teeth'),
    path('clinic11/', urology, name='urology'),
    path('reserve/<id>', reserve, name='reserve'),


    path('', views.home, name='Home'),
    path('profile', views.profile),
    path('MoreServ', views.more_serv, name='more_serv'),


    path('Login', LoginView.as_view(
        template_name="LOGIN/index.html"), name='login'),

    path('logout', LogoutView.as_view(
        template_name='Home/home.html'), name='logout'),

    path('فيزيتا', views.arabic, name='arabic'),
    path('إشترك', views.ARsingup, name='ARsignup'),
    path('تسجيل الدخول', views.ARlogin, name='ARlogin'),
    path('ticket/<id>', views.Ticket, name='ticket'),
    path('forgetEmail', views.forgetEmail, name='forgetEmail'),

    # Dashboard Action
    path('delete/<depid>', deletedepartment, name="deletedepartment"),
    path('search_dep', searchdepartment, name="search_dep"),

    path('searchticket', searchticket, name='searchticket'),

    path('update/<id>', editdepartment, name='edit_department'),
    path('updatedepartment/<id>', updatedepartment, name='updatedepartment'),
    path('deletepatient/<p_id>', deletepatient, name="deletepatient"),
    path('searchpatient', searchpatient, name='searchpatient'),
    path('showclinc/<id>',showclinc, name='showclinc'),
    path('editpatient/<id>',editpatient,name="editpatient"),
    path('updatepatient/<id>',updatepatient,name="updatepatient"),
    path('newfeedback', add_Feedback, name='newfeedback'),
    path('deletedoctor/<d_id>', deletedoctor, name="deletedoctor"),
    path('searchdoctor', searchdoctor, name='searchdoctor'),
    path('editdoctor/<id>',editdoctor,name="editdoctor"),
    path('updatedoctor/<id>',updatedoctor,name="updatedoctor"),

    path('view-ticket/<id>',viewticket,name='view-ticket'),
    path('sum_all_ticket',sumticket, name='sum_all_ticket')
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
