from django.db import models
# Create your models here.
class Enquiry(models.Model):
    iss=(("tech","Technical"),("product","Product"),("shop","Shop"))
    name=models.CharField(max_length=30)
    phone =models.CharField(max_length=12)
    email=models.EmailField()
    issue=models.CharField(max_length=10,choices=iss)
    message=models.TextField()


class RC(models.Model):
    name=models.CharField(max_length=30)
    phone = models.CharField(max_length=12)

class Product(models.Model):
    brand=models.CharField(max_length=100)
    products=models.CharField(max_length=100)


class Feedback(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    feedback=models.TextField()
