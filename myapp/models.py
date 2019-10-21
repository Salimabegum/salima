from django.db import models

# Create your models here.

class Product_field(models.Model):
	name = models.CharField(max_length = 25)
	description = models.CharField(max_length = 25)
	cost = models.IntegerField()
	no_of_product = models.CharField(max_length = 25)

	def __str__(self):
		return self.name

class user_field(models.Model):
	Username = models.CharField(max_length = 25)
	email = models.EmailField()
	mobile = models.CharField(max_length = 10)
	Account_blnc = models.IntegerField()

	def __str__(self):
		return self.Username

class buyed(models.Model):
	product = models.ForeignKey(Product_field,on_delete=models.CASCADE)
	user = models.ForeignKey(user_field,on_delete=models.CASCADE)

	def __str__(self):
		return "{}---{}".format(self.product, self.user)



