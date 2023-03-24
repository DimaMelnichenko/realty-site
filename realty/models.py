from django.db import models


# Create your models here.


class RealtyObjects(models.Model):
    type = models.CharField(max_length=100)
    cost = models.IntegerField(default=0)
    address = models.CharField(max_length=1000)

    def __str__(self):
        return self.type + ' ' + self.address
