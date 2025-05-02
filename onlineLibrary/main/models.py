from django.db import models
from django.utils import timezone

class Reader(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    date_of_registration = models.DateField(default=timezone.now)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=15)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.surname} ({self.email})"
