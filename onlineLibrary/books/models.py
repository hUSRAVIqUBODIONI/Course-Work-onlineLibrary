from django.db import models
from main.models import Reader  # Импорт Reader модели из приложения main
from django.utils import timezone


# Модель для авторов
class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=100)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


# Модель для жанров
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Модель для книг
class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    date_of_publish = models.DateField(null=True, blank=True)
    authors = models.ManyToManyField(Author, related_name="books")
    genres = models.ManyToManyField(Genre, related_name="books")

    def __str__(self):
        return self.title


# Модель для экземпляров книг
class Exampler(models.Model):
    inventory_number = models.IntegerField(unique=True, blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='exemplars')
    condition = models.CharField(max_length=100)

    # Логика автогенерации номера экземпляра
    def save(self, *args, **kwargs):
        if self.inventory_number is None:
            last = Exampler.objects.order_by('-inventory_number').first()
            self.inventory_number = (last.inventory_number + 1) if last else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Экземпляр {self.inventory_number} — {self.book.title} ({self.condition})"


# Модель для выдачи книг
class Issuance(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, related_name='issuances')
    exampler = models.ForeignKey(Exampler, on_delete=models.CASCADE, related_name='issuances')
    issuance_date = models.DateField(default=timezone.now)
    return_date = models.DateField(default=timezone.now() + timezone.timedelta(weeks=2))
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return f"{self.reader.name} {self.reader.surname} - {self.exampler.book.title}"

    class Meta:
        unique_together = ('reader', 'exampler')
