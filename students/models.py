from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
year = [(str(year),year) for year in range(2018,datetime.date.today().year+1)]

class Course(models.Model):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

class Group(models.Model):
    name = models.CharField(max_length=100)
    join_date = models.DateField(default=timezone.now)
    batch = models.CharField(choices=year,max_length=10,default=datetime.date.today().year)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name+" "+self.batch


class Admission(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField(null=True,blank=True)
    contact = models.CharField(null=True,blank=True,max_length=20)
    college = models.CharField(max_length=100,null=True,blank=True)
    dob = models.DateField(blank=True,null=True)
    course_enrolled = models.ForeignKey(Course,on_delete=models.CASCADE)
    remarks = models.TextField(null=True,blank=True)
    group = models.ForeignKey(Group,on_delete=models.CASCADE,default=1)
    counseller = models.CharField(null=True,blank=True,default="Dipendra KM",max_length=20)

    def __str__(self):
        return self.student_name


