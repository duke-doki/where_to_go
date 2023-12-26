# Generated by Django 4.2.8 on 2023-12-26 07:24
import json
import os
import requests
from django.core.files.base import ContentFile
from django.db import migrations, transaction


def add_images(apps, schema_editor):
    Place = apps.get_model('places', 'Place')
    Image = apps.get_model('places', 'Image')
    directory = 'static/places'
    os.makedirs('images', exist_ok=True)
    for json_file in os.listdir(directory):
        with open(os.path.join(directory, json_file)) as file:
            json_place = json.load(file)
        images_urls = json_place['imgs']
        with transaction.atomic():
            place = Place.objects.get(title=json_place['title'])
            for index, image_url in enumerate(images_urls, start=1):
                image = Image.objects.create(
                    url=image_url,
                    place=place,
                    number=index
                )
                response = requests.get(image_url)
                image.picture.save(
                    f'images/{json_place["title"]}{index}.jpg',
                    ContentFile(response.content),
                    save=True
                )


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_image_url'),
    ]

    operations = [
        migrations.RunPython(add_images)
    ]
