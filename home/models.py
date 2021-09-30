from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=50)
    uemail= models.EmailField(max_length=50)
    upassword = models.CharField(max_length=100)
    uphone = models.IntegerField()
    uviews = models.CharField(max_length=200)
    
    def __str__(self):
        return self.uname