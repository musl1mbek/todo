from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255)
    tick = models.BooleanField(default=False)
    text = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


class Cash(models.Model):
    money = models.IntegerField(default=0)
