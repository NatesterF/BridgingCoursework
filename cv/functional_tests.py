from selenium import webdriver
import unittest

class CVTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000/cv')
    def test_checK_title(self):
        self.assertIn('CV', self.browser.title)
        

unittest.main(warnings='ignore') 
