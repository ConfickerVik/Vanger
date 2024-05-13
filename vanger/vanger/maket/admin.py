from django.contrib import admin
from .models import SliderImage
from adminsortable2.admin import SortableAdminMixin


@admin.register(SliderImage)
class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ["my_order", "name", "cover"]
