from django.db import models


# Create your models here.
class Place(models.Model):
    title = models.CharField(
        'Место',
        max_length=100
    )
    description_short = models.TextField(
        'Короткое описание',
        null=True, blank=True
    )
    description_long = models.TextField(
        'Длинное описание',
        null=True, blank=True
    )
    coordinates = models.JSONField(
        'Координаты',
        null=True, blank=True
    )

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
        null=True, blank=True
    )

    def __str__(self):
        return f'{self.number} {self.place.title}'
