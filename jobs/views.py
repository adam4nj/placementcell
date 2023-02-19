from django.shortcuts import render

# Create your views here.

from .models import Job

def joblist(request):
    context = {
        'jobs': Job.objects.all()
    }
    return render(request, 'jobs/jobs.html', context)
