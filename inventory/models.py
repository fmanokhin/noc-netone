from django.db import models

# Create your models here.
# Модель точки присутствия
class Pop(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contacts = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    bandwidth = models.CharField(max_length=100)
    vlans = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)

    def new_pop(self):
        self.save()

    def __str__(self):
        return self.title