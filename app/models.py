from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField()
    image = models.ImageField()
    link = models.CharField()
    text = models.TextField()

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField()
    text = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField()
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.name