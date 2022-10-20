from django.shortcuts import render
from .models import Photo
# Create your views here.

def home(request):
    context = {'photos':Photo.objects.all()}
    return render(request, 'base/home.html', context)
