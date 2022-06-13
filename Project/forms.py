# from cv2 import DrawMatchesFlags_DEFAULT
from django import forms
from Admin.models import Patient, feedback, ticket


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = '__all__'
        labels = {
            'National_num': 'National_ID'
        }
        widgets = {
            'BirthDay': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class ticketForm(forms.ModelForm):
    class Meta:
        model = ticket
        fields = '__all__'

class Feedform(forms.ModelForm):
    class Meta:
        model = feedback
        exclude = {'Feedback'}
