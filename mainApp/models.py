from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=250)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories')

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='subcategories', null=True,blank=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name