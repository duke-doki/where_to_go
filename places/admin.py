from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin
from places.models import Place, Image
from adminsortable2.admin import SortableTabularInline
from adminsortable2.admin import SortableAdminBase


class ImageInline(SortableTabularInline):
    model = Image
    readonly_fields = ["pic", ]
    fields = ("picture", "pic", "number")
    def pic(model, obj):
        k = obj.picture.width / obj.picture.height
        return mark_safe(
            f'<'
            f'img src="{obj.picture.url}" '
            f'width="{k * 200}" '
            f'height={200} '
            f'/>'
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', )
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ('place', )
    readonly_fields = ["pic", ]

    def pic(self, obj):
        k = obj.picture.width / obj.picture.height
        return mark_safe(
            f'<'
            f'img src="{obj.picture.url}" '
            f'width="{k * 200}" '
            f'height={200} '
            f'/>'
        )
