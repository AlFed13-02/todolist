from django.db import models
from django.conf import settings


class Task(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    to_do = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    done = models.BooleanField(default=False)

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return self.to_do
