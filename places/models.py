from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        'Место',
        max_length=100
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
        null=True, blank=True
    )
    lat = models.FloatField(
        'Широта',
        null=True, blank=True
    )

    def coordinates(self):
        coordinates_json = {
            "lng": self.lng,
            "lat": self.lat
        }
        return coordinates_json

    def __str__(self):
        return self.title


class Image(models.Model):
    picture = models.ImageField(
        'Картинка',
        blank=True
    )
    place = models.ForeignKey(
        Place,
        verbose_name='Связь с местом',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='images'
    )
    number = models.IntegerField(
        'Номер',
        null=True, blank=True,
        db_index=True
    )

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.number} {self.place.title}'
