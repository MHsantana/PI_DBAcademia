from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=101)
    cnpj = models.CharField(max_length=20, blank=True, null=True)
    headquarter = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    tel2 = models.CharField(max_length=20, blank=True, null=True)
    branch = models.BooleanField(default=False)
    maintenance = models.DateField(blank=True, null=True)
    #created_at = models.DateTimeField(auto_now_add=True)