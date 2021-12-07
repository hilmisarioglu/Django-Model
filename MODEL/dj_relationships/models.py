from django.db import models

# Create your models here.

class Creator(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.first_name

class Language(models.Model):
    name = models.CharField(max_length=10)
    creator = models.ForeignKey(Creator , on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Boolean(models.Model):
    boolean = models.BooleanField()