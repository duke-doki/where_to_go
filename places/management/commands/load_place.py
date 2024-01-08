import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):

    def handle(self, *args, **options):
        link = options['link']
        response = requests.get(link)
        response.raise_for_status()
        json_place = response.json()
        place = Place.objects.create(
            title=json_place['title'],
            short_description=json_place['description_short'],
            long_description=json_place['description_long'],
            lng=json_place['coordinates']['lng'],
            lat=json_place['coordinates']['lat']
        )
        images_urls = json_place['imgs']
        for index, image_url in enumerate(images_urls, start=1):
            image = Image.objects.create(
                place=place,
                number=index
            )
            response = requests.get(image_url)
            response.raise_for_status()
            image.picture.save(
                f'{json_place["title"]}{index}.jpg',
                ContentFile(response.content),
                save=True
            )

    def add_arguments(self, parser):
        parser.add_argument('link', type=str, help='The link to json')
