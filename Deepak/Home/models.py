from datetime import date
from select import select
from tokenize import Name, Number
from django.db import models

# Create your models here.
class Contact(models.Model):
      Name = models.CharField(max_length=122)
      Email = models.CharField(max_length=122)
      Number = models.CharField(max_length=12)
      select = models.CharField(max_length=1)
      date = models.DateField()
