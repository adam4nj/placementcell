from django.shortcuts import render

# Create your views here.

from .models import Job

def home(request):
    return render(request,'jobs/home.html')

def about(request):
    return render(request,'jobs/about.html')

def joblist(request):
    context = {
        'jobs': Job.objects.all()
    }
    return render(request, 'jobs/jobs.html', context)

def contact(request):
    return render(request,'jobs/contact.html')
