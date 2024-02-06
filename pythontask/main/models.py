from django.db import models
from datetime import datetime


class Task(models.Model):
    title = models.CharField(
        'Название', max_length=29,
    )
    text = models.TextField(
        "Описание",
    )

    def __str__(self):
        return self.title


class Appointment(models.Model):
    date = models.DateTimeField(
        default=datetime.utcnow,
    )
    client_name = models.CharField(
        max_length=29,
    )
    message = models.TextField()

