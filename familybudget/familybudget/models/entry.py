from django.contrib.auth.models import User
from django.db import models

from .category import Category
from .list import List

class Entry(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    amount = models.FloatField()
    categories = models.ManyToManyField(Category)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
