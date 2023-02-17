from django.db import models
from django.utils import timezone
from users.models import CustomUser,Company

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(max_length=10)


    def __str__(self):
        return self.title


