from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=15,null=True)
    gender=models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.user.username
class Add(models.Model):
    NUser=models.ForeignKey(NUser,on_delete=models.CASCADE)
    date=models.DateField()
    itemname=models.CharField(max_length=100,null=True)
    itemquantity=models.CharField(max_length=10,null=True)
    status=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.itemname
