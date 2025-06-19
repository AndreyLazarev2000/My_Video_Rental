from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    length = models.PositiveIntegerField(help_text="Длительность фильма в минутах")
    release_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"