from django.db import models
from uuid import uuid4
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('mail address is required')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email)

        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, username, email, password):

        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser,PermissionsMixin):
    userId = models.CharField(
        max_length=255, default=uuid4, primary_key=True, editable=False, unique=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    created = models.DateTimeField(default=timezone.now)

    is_student = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)


    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField()
    student_fname = models.CharField(max_length=10)
    student_lname = models.CharField(max_length=10)
    dob = models.DateField(max_length=10)
    age = models.SmallIntegerField()
    address = models.TextField(max_length=50)
    district = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    pin = models.PositiveIntegerField()
    ph_no = models.PositiveIntegerField()
    


    def __str__(self):
        return self.user.email


class Company(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    email = models.EmailField()
    c_name = models.CharField(max_length=10)
    address = models.TextField(max_length=50)
    district = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    pin = models.PositiveIntegerField()
    ph_no = models.PositiveIntegerField()

    description = models.CharField(max_length=255)

    def __str__(self):
        return self.user.email



