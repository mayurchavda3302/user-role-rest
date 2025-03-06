from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=8)

    def __str__(self):
        return self.username
    


class Role(models.Model):
    role_name=models.CharField(max_length=20)
    access_modules=models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)
    is_actvie=models.BooleanField(default=True)
    
'''
{
"role_name":"admin",
"access_modules":"dashboard"
}
'''

class User(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()   
    password=models.CharField(max_length=10)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)   
'''
    "first_name":"mayur",
    "last_name":"chavda",
    "email":"mayurchavda12@gmail.com",
    "password":"mayur123",
    "role":1
'''