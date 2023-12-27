from django.contrib import admin
from django.utils.safestring import mark_safe

from places.models import Place, Image


# Register your models here.
class ImageInline(admin.TabularInline):
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
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', )
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_filter = ('place', )
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
