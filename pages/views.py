from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image

# Create your views here.
def homePageView(request):
    try:
        with open("app/image.jpeg", "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        red = Image.new('RGBA', (1, 1), (255,0,0,0))
        response = HttpResponse(content_type="image/jpeg")
        red.save(response, "JPEG")
        return response