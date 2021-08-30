from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class CollegeModel(models.Model):
    cname=models.CharField(primary_key=True,unique=True,max_length=100)
    c_address=models.CharField(max_length=200)

    def __str__(self):
        return self.cname

class DepartmentModel(models.Model):
    d_no=models.IntegerField(primary_key=True)
    clg=models.ForeignKey(CollegeModel,on_delete=models.CASCADE)
    dep_name=models.CharField(max_length=100)

    def __str__(self):
        return self.dep_name


class LecturerModel(models.Model):
    lecturer_id=models.IntegerField(primary_key=True,unique=True)
    clg=models.ForeignKey(CollegeModel,on_delete=models.CASCADE)
    l_name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    depname =models.ManyToManyField(DepartmentModel)

    def __str__(self):
        return self.l_name


class StudentModel(models.Model):
    rollno=models.IntegerField(primary_key=True,unique=True)
    s_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=150,unique=True)
    lname=models.ForeignKey(LecturerModel,on_delete=models.CASCADE)
    clg=models.ForeignKey(CollegeModel,on_delete=models.CASCADE)
    dep=models.ForeignKey(DepartmentModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.s_name
