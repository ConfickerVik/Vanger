from django.shortcuts import render
from .models import SliderImage


def index(requests):
    image_collection = SliderImage.objects.all()#.values_list("cover__file", flat=True)
    return render(requests, 'index.html', context={'images': image_collection})
