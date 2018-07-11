from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length = 250,primary_key = True)
	cost = models.IntegerField()
	id = models.IntegerField()
	class Meta:
		db_table = "product"

class Customer(models.Model):
	name = models.CharField(max_length = 250)
	address = models.TextField()

	class Meta:
		db_table = "customer"

class Salesorder(models.Model):
	salesorder_types = [('online',"online payment"),('COD',"cash on delivery")]
	sale_type = models.CharField(max_length = 6,choices = salesorder_types)
	name = models.CharField(max_length = 250)
	product = models.ManyToManyField(Product)
	customer = models.ForeignKey(Customer,on_delete = None)


	class Meta:
		db_table = "salesorders"