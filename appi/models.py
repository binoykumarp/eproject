from django.db import models


employee=[
    {"id":1,"name":"narjas","dept":"cs"},
    {"id":2,"name":"surjas","dept":"eee"},
    {"id":3,"name":"murjas","dept":"mech"},
    {"id":4,"name":"shifas","dept":"cs"},
    {"id":5,"name":"anas","dept":"eee"},
]

manager=[
    {"id":1,"name":"narjas","exp":3},
    {"id":2,"name":"munna","exp":4},
    {"id":3,"name":"chinnu","exp":5},
    {"id":4,"name":"kunju","exp":3},
    {"id":5,"name":"bichus","exp":2},
]
# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)


class Manager(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    experience=models.IntegerField(null=True)
    profile=models.ImageField(upload_to="manager_pic")