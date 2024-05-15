from django.db import models
from filer.fields.image import FilerImageField


class SliderImage(models.Model):
    name = models.CharField(max_length=64)

    sort = models.PositiveIntegerField(default=0)

    cover = FilerImageField(related_name="image_covers", on_delete=models.CASCADE)

    class Meta:
        ordering = ['sort']
