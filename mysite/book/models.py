from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(
        max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField(max_length=13, help_text='13 charecter')
    genre = models.ManyToManyField(
        Genre, help_text='Select a genre for this Book')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_birth = models.DateField('Died', null=True, blank=True)

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)
