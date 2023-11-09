from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('executor', args=[self.name])

class Executor(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_of_foundation = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    slug = models.SlugField(max_length=255, blank=True, unique=True, db_index=True, verbose_name='URL')


    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.name}-{self.surname}-{self.date_of_foundation}")
        super(Executor, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}-{self.date_of_foundation}"

    def get_absolute_url(self):
        return reverse('detail', args=(self.genre, self.slug, ))
