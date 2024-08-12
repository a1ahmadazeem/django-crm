from django.db import models

class Record (models.Model):
    creation_date=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=80)
    last_name=models.CharField(max_length=80)
    email  =models.EmailField()
    phone=models.CharField(max_length=80)
    address=models.CharField(max_length=300)
    city =models.CharField(max_length=80)
    province=models.CharField(max_length=80)
    country=models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name + "   " + self.last_name
    
    
    
    
    
    
