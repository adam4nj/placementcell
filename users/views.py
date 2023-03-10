from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from .forms import StudentSignUpForm,StudentProfileForm, CompanySignUpForm, CompanyProfileForm
from .models import CustomUser
# Create your views here.

class StudentSignUpView(CreateView):
    model = CustomUser
    form_classes = {
        's_signup': StudentSignUpForm,
        's_profile': StudentProfileForm,
    }
    fields = []
    template_name = 'users/signup-student.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

class CompanySignUpView(CreateView):
    model = CustomUser
    form_classes = {
        'c_signup': CompanySignUpForm,
        'c_profile': CompanyProfileForm,
    }
    fields = []
    template_name = 'users/signup-company.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

