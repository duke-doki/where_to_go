from adminsortable2.admin import SortableAdminBase
from adminsortable2.admin import SortableTabularInline
from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image


class ImageInline(SortableTabularInline):
    model = Image
    readonly_fields = ["get_pic", ]
    fields = ("picture", "get_pic", "number")

    def get_pic(self, image):
        return format_html(
            '<img src="{}" style="max-width:200px; max-height:200px" />',
            image.picture.url
        )

    get_pic.short_description = "Preview"


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', )
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ('place', )
    readonly_fields = ["get_pic", ]

    def get_pic(self, image):
        return format_html(
            '<img src="{}" style="max-width:200px; max-height:200px" />',
            image.picture.url
        )

    get_pic.short_description = "Preview"
