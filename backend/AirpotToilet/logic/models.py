from django.db import models

# Create your models here.
class Feedback(models.Model):
    Fid = models.AutoField(primary_key=True)
    Value = models.CharField(max_length=10)

class Staff(models.Model):
    Sid = models.AutoField(primary_key=True)
    Sname = models.CharField(max_length=250)
    Phone = models.CharField(max_length = 10)
    Address = models.CharField(max_length=250)

class Day(models.Model):
    Did = models.AutoField(primary_key=True)
    Day = models.CharField(max_length=250)

class Allocation(models.Model):
    Aid = models.AutoField(primary_key=True)
    Sid = models.ForeignKey(Staff, on_delete = models.CASCADE)
    Did = models.ForeignKey(Day, on_delete = models.CASCADE)