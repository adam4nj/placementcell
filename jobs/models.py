from django.db import models
from django.utils import timezone
from users.models import Student, Company

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=20)
    date_posted = models.DateTimeField(default=timezone.now)
    last_date = models.DateField()
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField()
    desc = models.TextField()

    def __str__(self):
        return self.title
    
class Job_apply(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    OPTIONS = (
        ('0', 'Accepted'),
        ('1', 'Pending'),
        ('2', 'Rejected'),
    )
    status = models.CharField(max_length=1,choices=OPTIONS,default='1')
    
    def __str__(self):
        return self.job



    



