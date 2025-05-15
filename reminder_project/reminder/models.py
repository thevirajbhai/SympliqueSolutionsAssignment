from django.db import models

class Reminder(models.Model):
    datetime = models.DateTimeField()
    message = models.TextField()
    method = models.CharField(max_length=10, choices=[('sms', 'SMS'), ('email', 'Email')])

    def __str__(self):
        return f"{self.datetime} - {self.method}"
