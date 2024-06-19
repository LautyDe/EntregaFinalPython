from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curse(models.Model):
  name = models.CharField(max_length=40)
  category = models.IntegerField()
  def __str__(self):
    return f'{self.name} - {self.category}'
  class Meta():
    ordering = ('name','category')
    unique_together = ('name','category',)
  
class Student(models.Model):
  name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(null=True)
  def __str__(self):
    return f'{self.name} - {self.last_name}'

class Teacher(models.Model):
  name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField()
  profession = models.CharField(max_length=30)
  curses = models.ManyToManyField(Curse)
  def __str__(self):
    return f'{self.name} {self.last_name} - {self.profession}'

class Works(models.Model):
  name = models.CharField(max_length=30)
  date = models.DateField()
  delivered = models.BooleanField()
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  def __str__(self):
    return f'{self.name} - {self.date}'
  class Meta():
    #verbose_name = 'Works' Como aparece en la lista del admin
    verbose_name_plural = 'Works' #el plural del modelo

class Avatar(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  image = models.ImageField(upload_to = 'avatares', blank = True, null = True)