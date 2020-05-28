from django.db import models

# Create your models here.
class BankBranch(models.Model):
	bank = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.CharField(max_length=100)

	def __str__(self):
		return self.bank.capitalize() + "-" + self.address


