from django.contrib import admin

from places.models import Place, Image


# Register your models here.
class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', )
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_filter = ('place', )
