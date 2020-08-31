from .models import CvItem 
from django.shortcuts import render
from django.utils import timezone
from django.contrib import admin
import mimetypes

def cv(request):
    CVItems = CvItem.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #CVItems = CvItem.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'cv/cv.html', {'CVItems': CVItems})


