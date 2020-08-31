from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class CVTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000/cv')
   # def test_checK_title(self):
   #     self.assertIn('CV', self.browser.title)
   # def test_check_contains_name(self):
   #     element=self.browser.find_element(By.XPATH,"//*[contains(.,'Nathan Flaherty')]")
   #     self.assertNotEquals(element,None)
   # def test_check_contains_uni(self):
   #     element=self.browser.find_element(By.XPATH,"//*[contains(.,'University Of Birmingham')]")
   #     self.assertNotEquals(element,None)
   # def test_blog_link(self):
   #     try:
   #         blog_button = self.browser.find_element_by_link_text("Nathan Flaherty's CS Blog")
   #     except (NoSuchElementException):
   #         self.fail()

   #     blog_button.click()
   #     

   
   # def test_cv_download_link(self):
   #     try:
   #         blog_button = self.browser.find_element_by_link_text("Download CV as PDF")
   #     except (NoSuchElementException):
   #         self.fail()

   #     blog_button.click()

unittest.main(warnings='ignore') 

