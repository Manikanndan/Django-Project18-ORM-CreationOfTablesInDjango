from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.topic_name

class webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()

    def __str__(self):
        return self.name

class Access_Record(models.Model):
    name=models.ForeignKey(webpage,on_delete=models.CASCADE)
    date=models.DateField()


class course(models.Model):
    cid=models.IntegerField(primary_key=True)
    coursename=models.CharField(max_length=100)
    trainer=models.CharField(max_length=50)

    def __str__(self):
        return self.coursename

class student(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=50)
    email=models.CharField(max_length=100,unique=True)
    courseid=models.ForeignKey(course,on_delete=models.CASCADE)

    def __str__(self):
        return self.sname

class bonus(models.Model):
    Ename=models.CharField(max_length=10)
    Job=models.CharField(max_length=9)
    Sal=models.IntegerField()
    Comm=models.IntegerField()

    def __str__(self):
        return self.Ename

class Salgrade(models.Model):
    grade=models.IntegerField()
    losal=models.IntegerField()
    hisal=models.IntegerField()

class Department(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=14)
    loc=models.CharField(max_length=13)

    def __str__(self):
        return self.dname

class Employee(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=10)
    job=models.CharField(max_length=9)
    mgr=models.IntegerField()
    hiredate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField()
    deptno=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename
