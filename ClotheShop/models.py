from django.db import models

# Create your models here.
class Shoe(models.Model):
  model = models.CharField(max_length=100)
  size = models.IntegerField()
  price = models.IntegerField()
  def __str__(self):
    return f'{self.model} - {self.size}'
  class Meta():
    ordering = ('model','size')
  
class Shirt(models.Model):
  model = models.CharField(max_length=100)
  size = models.IntegerField()
  price = models.IntegerField()
  def __str__(self):
    return f'{self.model} - {self.size}'
  class Meta():
    ordering = ('model','size')

class User(models.Model):
  name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField()
  shoes = models.ForeignKey(Shoe, null=True, blank=True, on_delete=models.CASCADE)
  shirts = models.ForeignKey(Shirt, null=True, blank=True, on_delete=models.CASCADE)
  def __str__(self):
    return f'{self.name} {self.last_name}'