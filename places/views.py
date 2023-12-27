from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from places.models import Place
import urllib.parse

def index(request):
    legends = Place.objects.get(id=1)
    roofs = Place.objects.get(id=2)
    places_json = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": list(legends.coordinates.values())
                },
                "properties": {
                    "title": legends.title,
                    "placeId": "moscow_legends",
                    "detailsUrl": "static/places/moscow_legends.json"
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": list(roofs.coordinates.values())
                },
                "properties": {
                    "title": roofs.title,
                    "placeId": "roofs24",
                    "detailsUrl": "static/places/roofs24.json"
                }
            }
        ]
    }
    data = {'places_json': places_json, }
    return render(request, "index.html", context=data)


def place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_info = {
        "title": place.title,
        "imgs": [
            urllib.parse.unquote(img.picture.url) for img in place.images.all()
        ],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": place.coordinates
    }
    response = JsonResponse(
        place_info,
        safe=False,
        json_dumps_params={'ensure_ascii': False, 'indent': 2}
    )
    return response
