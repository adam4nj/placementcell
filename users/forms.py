from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import CustomUser, Student, Company

#Student

class StudentSignUpForm(UserCreationForm):
    pass
        
    class Meta:
        model = CustomUser
        fields = ["email", "password1", "password2"]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        Student.objects.create(user=user)
        return user
    
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['address','district','state','pin','ph_no']

#Company
        
class CompanySignUpForm(UserCreationForm):
    pass
        
    class Meta:
        model = CustomUser
        fields = ["email", "password1", "password2"]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_company = True
        user.save()
        Company.objects.create(user=user)
        return user
    
class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['c_name','address','district','state','pin','ph_no']




