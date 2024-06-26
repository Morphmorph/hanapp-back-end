from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)
import os
# Create your models here.
class UserManager(BaseUserManager):  
    def create_user(self,usertype,email,password='none'):
        if not email:
            raise ValueError('Email is not valid')
        if usertype is None:
            raise TypeError('User Should Have A Usertype')
        email = self.normalize_email(email)
        user = self.model(usertype = usertype,email = email)
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser,PermissionsMixin):
    email= models.EmailField(max_length=255,unique=True)
    usertype = models.TextField(choices=[('Employer','Employer'),('Student','Student')])
    is_Verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    otp = models.TextField(blank=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['usertype','password']

    objects = UserManager()

    def __str__(self):
        return self.email


def upload_to_static_images(instance, filename):
    basename, extension = os.path.splitext(filename)
    new_filename = f'{basename}{extension}'
    return os.path.join('images', new_filename)
def upload_to_static(instance, filename):
    return 'images/' + filename


class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    mid_name = models.CharField(max_length=64)
    suff_name = models.CharField(max_length=64,null=True,blank=True)
    birthday = models.DateField()
    age = models.CharField(max_length=12)
    contact_no = models.CharField(max_length=12)
    profile = models.ImageField(blank=True,null=True)

class Guardian(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    g_name = models.CharField(max_length=64)
    g_contact_no = models.CharField(max_length=12)
    g_address = models.CharField(max_length=64)

class EducationBg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sch_name = models.CharField(max_length=64)
    sch_address = models.CharField(max_length=64)
    course = models.CharField(max_length=64)
    year_level = models.CharField(max_length=64)

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comp_name = models.CharField(max_length=64)
    establish_date = models.DateField()
    website_url = models.URLField(max_length=100)
    comp_desc = models.TextField()

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    province = models.CharField(max_length=64)
    zipcode = models.CharField(max_length=12)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    looking_for = models.CharField(max_length=64)
    job_desc = models.TextField()
    job_type = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    status = models.CharField(max_length=5, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    salary = models.TextField()
    rate = models.CharField(max_length=24)

class Apply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cor = models.FileField(null=False,blank=False,upload_to='applicant/files')
    school_id = models.ImageField(null=False,blank=False,upload_to='applicant/files')
    facebook = models.TextField(default='',null=False)
    cov_let = models.FileField(null=False,blank=False,upload_to='applicant/files')
    applied_at = models.DateTimeField(auto_now_add=True)

class Bookmark(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bookmark_at = models.DateTimeField(auto_now_add=True)

class Applicant(models.Model):
    apply = models.ForeignKey(Apply, on_delete=models.CASCADE)
    status = models.CharField(max_length=24)
    date = models.DateTimeField(auto_now_add=True)

class Schedule(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    interview_type = models.CharField(max_length=24)
    method = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.CharField(max_length=5)
    end_time = models.CharField(max_length=5)