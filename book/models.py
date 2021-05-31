from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=150)
    price=models.IntegerField(max_length=20)
    cover=models.ImageField()


    class Meta:
        db_table='book'

    def __str__(self):
        return self.name
