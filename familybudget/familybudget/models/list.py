from django.contrib.auth.models import User
from django.db import models

class List(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    name = models.CharField(max_length=30)
    sharers = models.ManyToManyField(User)
