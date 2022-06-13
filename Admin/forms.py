
from django import forms
from .models import Department, Doctor, Patient, ticket


class clincform(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'form-control'}),
            'Days': forms.TextInput(attrs={'class': 'form-control'}),
            'Days2': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price Per LE'}),
        }


class patientform(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'National_num': forms.TextInput(attrs={'class': 'form-control'}),
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'BirthDay': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'City': forms.Select(attrs={'class': 'form-control'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control'})
        }

class ticketform(forms.ModelForm):
    class Meta:
        model = ticket
        fields = '__all__'
        widgets = {
            'dept': forms.Select(attrs={'class': 'form-control'}),
            'Pat': forms.Select(attrs={'class': 'form-control'}),
            'startdate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'enddate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class doctorform(forms.ModelForm):
      class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'City': forms.Select(attrs={'class': 'form-control'}),
            'dept':  forms.Select(attrs={'class': 'form-control'}),
            'Phone': forms.DateInput(attrs={'class': 'form-control', 'type': 'number'}),
           
        }    
