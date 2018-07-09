from django.db import models

# Create your models here.

class Pop(models.Model):
    title = models.CharField(max_length=200)
    address = models.TextField()
    contacts = models.TextField()
    manager = models.TextField()
    bandwidth = models.TextField()
    vlans = models.TextField()
    comments = models.TextField()

    def new_pop(self):
        self.save()

    def __str__(self):
        return self.title
