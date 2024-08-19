from django.db import models

# Create your models here.



class Links(models.Model):
    ru_name = models.CharField(max_length=50)
    kg_name = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    
    
    
class Contats(models.Model):
    ru_name = models.CharField(max_length=50)
    kg_name = models.CharField(max_length=50)
    link = models.CharField(max_length=255)