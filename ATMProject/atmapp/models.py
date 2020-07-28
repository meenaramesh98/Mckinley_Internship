from django.db import models

# Create your models here.

class AtmPinRegister(models.Model):
    username = models.CharField(max_length=50)
    cardnumber = models.CharField(max_length=50)
    pin = models.CharField(max_length=50)
    balance = models.CharField(max_length=50,default ='100000')
    
    def __str__(self):
        return self.name
        
        
class Transaction(models.Model):
    username = models.ForeignKey(AtmPinRegister, on_delete = models.CASCADE)
    transaction_method = models.CharField(max_length=50)
    transactionamount = models.CharField(max_length=50)
   
    
