from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TODO(models.Model):
    status_choices= [
        ('C', 'COMPLETE'),
        ('P', 'PENDING')
    ]
    priority_choices= [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10','10'),
    ]
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title= models.CharField(max_length=300)
    status= models.CharField(max_length=2, choices= status_choices)
    date= models.DateTimeField(auto_now_add=True)
    priority= models.CharField(max_length=2, choices= priority_choices) 



