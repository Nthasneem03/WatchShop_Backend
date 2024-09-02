from django.db import models

# Create your models here.

class Watch(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(upload_to='watches/',null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name