from django.db import models

# Create your models here.

#Food Model
class Food(models.Model):
    typeOfFood = models.CharField(max_length = 64)
    flavor = models.CharField(max_length = 64)
    size = models.CharField(max_length = 64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.id} - {self.typeOfFood} - {self.flavor} - {self.size} - {self.price}"