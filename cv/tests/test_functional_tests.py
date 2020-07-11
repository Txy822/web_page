from django.test import TestCase
from selenium import webdriver
import unittest

class FunctionalTestCase(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    def test_there_is_homepage(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Personal Blogs',self.browser.page_source)
    def tearDown(self):
        self.browser.quit()

    def test_hompage_title_exist(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('Tesfahun blog', self.browser.title)
        #self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away


if __name__ == '__main__':
    unittest.main(warnings='ignore')
