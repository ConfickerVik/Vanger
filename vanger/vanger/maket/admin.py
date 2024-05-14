from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django.utils.safestring import mark_safe

from .models import SliderImage


@admin.register(SliderImage)
class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ['image_thumb']
    list_display = ["my_order", "image_thumb",  "name", "cover"]

    def image_thumb(self, obj):
        if obj.cover:
            return mark_safe('<img src="%s" width="80px" height="80px" style="object-fit: contain;" />' % obj.cover.url)
        else:
            return 'None'

    image_thumb.short_description = 'Pictures'
