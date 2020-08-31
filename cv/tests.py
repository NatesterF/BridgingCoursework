from django.test import TestCase
from django.urls import resolve
from django.urls import reverse
from cv.views import cv


class URLTests(TestCase):
    def test_cv_url_returns_cv_view(self):
        found=resolve('/cv/') 
        self.assertEqual(found.func,cv)  
    

    def test_cv_url_uses_cv_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/cv.html')
        
    
