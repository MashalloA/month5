from django.db import models

class Director(models.Model):
    name = models.CharField(verbose_name="Autor's Name", max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(verbose_name="Movie Title", max_length=100)
    description = models.TextField(verbose_name="Movie Description", null=True, blank=True)
    duration = models.IntegerField(verbose_name="Movie Duration", default=0)
    director = models.ForeignKey(Director, verbose_name="Autor's name", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField(verbose_name="Review")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.text