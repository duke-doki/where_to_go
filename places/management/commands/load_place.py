import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):

    def handle(self, *args, **options):
        link = options['link']
        response = requests.get(link)
        response.raise_for_status()
        raw_place = response.json()
        place, is_found = Place.objects.get_or_create(
            title=raw_place['title'],
            defaults={
                'short_description': raw_place['description_short'],
                'long_description': raw_place['description_long'],
                'lng': raw_place['coordinates']['lng'],
                'lat': raw_place['coordinates']['lat']
            }
        )
        images_urls = raw_place['imgs']
        for index, image_url in enumerate(images_urls, start=1):
            response = requests.get(image_url)
            response.raise_for_status()
            content_file = ContentFile(
                response.content,
                f'{raw_place["title"]}{index}.jpg'
            )
            Image.objects.get_or_create(
                place=place,
                number=index,
                picture=content_file
            )

    def add_arguments(self, parser):
        parser.add_argument('link', type=str, help='The link to json')
