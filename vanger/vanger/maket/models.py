from django.db import models
from filer.fields.image import FilerImageField


class SliderImage(models.Model):
    name = models.CharField(max_length=255)

    my_order = models.PositiveIntegerField(
        default=0,
        db_index=True,
        editable=True,
        blank=False,
        null=False,
    )

    cover = FilerImageField(related_name="image_covers", null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['my_order']
