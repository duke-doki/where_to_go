from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        'Место',
        max_length=100,
        unique=True
    )
    short_description = models.TextField(
        'Короткое описание',
        blank=True
    )
    long_description = HTMLField(
        'Длинное описание',
        blank=True
    )
    lng = models.FloatField(
        'Долгота',
    )
    lat = models.FloatField(
        'Широта',
    )

    def __str__(self):
        return self.title

    def compile_coordinates(self):
        coordinates = {
            "lng": self.lng,
            "lat": self.lat
        }
        return coordinates


class Image(models.Model):
    picture = models.ImageField(
        'Картинка',
    )
    place = models.ForeignKey(
        Place,
        verbose_name='Связь с местом',
        on_delete=models.CASCADE,
        related_name='images'
    )
    number = models.IntegerField(
        'Номер',
        default=0,
        blank=True,
        db_index=True
    )

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.number} {self.place.title}'
