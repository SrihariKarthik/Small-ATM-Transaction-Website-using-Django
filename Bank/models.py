from django.db import models
from django.urls import reverse
# Create your models here.

class BankDB(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Account_Number =models.CharField(max_length=50)
    Bank_balance = models.IntegerField()

    


    def __str__(self):
        return(f" Mr/Mrs. {self.first_name} {self.last_name} with the account no: {self.Account_Number} has a bank balance of INR:{self.Bank_balance}")