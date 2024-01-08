import urllib.parse

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from places.models import Place


def index(request):
    all_places = Place.objects.all()
    places_json = {
        "type": "FeatureCollection",
        "features": [

        ]
    }
    for place_point in all_places:
        places_json["features"].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": list(place_point.coordinates.values())
                },
                "properties": {
                    "title": place_point.title,
                    "placeId": "moscow_legends",
                    "detailsUrl": reverse(place, args=[place_point.id])
                }
            }

        )

    data = {"places_json": places_json, }
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
        json_dumps_params={"ensure_ascii": False, "indent": 2}
    )
    return response
