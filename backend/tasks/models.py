from django.db import models
from django.conf.settings import AUTH_USER_MODEL


class Task(models.Model):
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    to_do = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    done = BooleanField(default=False)

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return self.to_do
