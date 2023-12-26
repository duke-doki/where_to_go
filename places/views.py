from django.shortcuts import render

from places.models import Place


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
