from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


def is_positive(value):
    if value<0:
        raise ValidationError("Enter the positive value")
# Create your models here.


class IncomeCategory(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Income(models.Model):
    title = models.CharField(max_length=100)
    rupes = models.FloatField(validators=[is_positive])
    bill_no = models.CharField(null=True,blank=True,max_length=100)
    biiling_file = models.FileField(null=True,blank=True,upload_to='income/')
    date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True,null=True)
    category = models.ForeignKey(IncomeCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ExpensesCategory(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Expenses(models.Model):
    title = models.CharField(max_length=100)
    rupes = models.FloatField(validators=[is_positive])
    checque = models.FileField(null=True,blank=True,upload_to='expenses/')
    date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True,null=True)
    category = models.ForeignKey(ExpensesCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.title