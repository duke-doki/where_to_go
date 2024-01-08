import urllib.parse

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from places.models import Place


def index(request):
    places = Place.objects.all()
    features = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": list(place_point.coordinates().values())
            },
            "properties": {
                "title": place_point.title,
                "placeId": "moscow_legends",
                "detailsUrl": reverse(get_place, args=[place_point.id])
            }
        }
        for place_point in places
    ]
    places_view = {
        "type": "FeatureCollection",
        "features": features
    }

    data = {"places_json": places_view, }
    return render(request, "index.html", context=data)


def get_place(request, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related('images'),
        id=place_id
    )
    place_info = {
        "title": place.title,
        "imgs": [
            urllib.parse.unquote(img.picture.url) for img in place.images.all()
        ],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": place.coordinates()
    }
    response = JsonResponse(
        place_info,
        safe=False,
        json_dumps_params={"ensure_ascii": False, "indent": 2}
    )
    return response
