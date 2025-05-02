from django.db import models

class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    date_of_publish = models.DateField(null=True, blank=True)
  


    def __str__(self):
        return f"{self.title} (ISBN: {self.isbn})"
