from django.db import models

# Create your models here.

class Quiz(models.Model):
    question = models.TextField()
    answer = models.BooleanField()
    correct = models.IntegerField(default=0)
    incorrect = models.IntegerField(default=0)
