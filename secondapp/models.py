from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)
    job = models.CharField(null=True, blank=True, max_length=100)
    age = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(null=True, blank=True, max_length=100)
    content = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title
