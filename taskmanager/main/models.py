from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.

class Task (models.Model):
    title = models.CharField(max_length=100)
    task  = models.TextField(validators=[MaxLengthValidator(100),])

    def __str__(self):
        return self.title