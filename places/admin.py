from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin
from places.models import Place, Image
from adminsortable2.admin import SortableTabularInline
from adminsortable2.admin import SortableAdminBase
from django.utils.html import format_html


class ImageInline(SortableTabularInline):
    model = Image
    readonly_fields = ["get_pic", ]
    fields = ("picture", "get_pic", "number")

    def get_pic(self, image):
        k = image.picture.width / image.picture.height
        return format_html(
            '<img src="{}" width="{}" height={} />',
            image.picture.url,
            k * 200,
            200
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
        k = image.picture.width / image.picture.height
        return format_html(
            '<img src="{}" width="{}" height={} />',
            image.picture.url,
            k * 200,
            200
        )

    get_pic.short_description = "Preview"
