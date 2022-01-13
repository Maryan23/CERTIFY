from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import *

class EmployerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    logo = CloudinaryField('logo')
    company_name = forms.CharField(required=True)
    about = forms.TextInput()
    tel_number = forms.IntegerField(required=True)
    reg_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_employer = True
        user.save()
        employer = Employer.objects.create(user=user)
        employer.logo = self.cleaned_data.get('logo')
        employer.company_name = self.cleaned_data.get('company_name')
        employer.about = self.cleaned_data.get('about')
        employer.tel_number = self.cleaned_data.get('tel_number')
        employer.reg_number = self.cleaned_data.get('reg_number')
        return employer

class InstitutionSignUpForm(UserCreationForm):
    email = forms.EmailField()
    reg_no = forms.CharField(required=True)
    institution_name = forms.CharField(required=True)
    location = forms.CharField(required=True)
    location_address = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_institution = True
        user.save()
        institution = Institution.objects.create(user=user)
        institution.reg_no = self.cleaned_data.get('reg_no')
        institution.institution_name = self.cleaned_data.get('institution_name')
        institution.location = self.cleaned_data.get('location')
        institution.location_address = self.cleaned_data.get('location_address')
        return institution