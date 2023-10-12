from django.db import models

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    district = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    account_type = models.CharField(max_length=20)
    materials_provide = models.TextField(null=True,blank=True)  

    def __str__(self):
        return self.name
