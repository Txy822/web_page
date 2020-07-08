from django.test import TestCase

# Create your tests here.
from .models import Cv


# Another Test: Entrys
#
# Did you notice that the pluralization of cv is misspelled in the admin interface? “cvs” should instead read “cvies”.
# Let’s write a test to verify that when Django correctly pluralizes “cv” to “cvies”.
class CvModelTest(TestCase):
    def test_title_str_representation(self):
        tit= Cv(title="mytitle")
        self.assertEqual(str(tit),tit.title)
    # def test_text_representation(self):
    #     tex= Cv(text="this is my text")
    #     self.assertEqual("this is my text",tex.text)
    def test_verbose_name_plural(self):
        #self.assertEqual(str(Cv._meta.verbose_name_plural), "cvs")
        self.assertEqual(str(Cv._meta.verbose_name_plural), "cvies")

#         Every site should have a homepage. Let’s write a failing test for that.
#
# We can use the Django test client to create a test to make sure
# that our homepage returns an HTTP 200 status code (this is the standard response for a successful HTTP request).
    def  test_homepage(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)

    # def test_one_entry(self):
    #     Cv.objects.create(title='1-title', text='1-body')
    #     response = self.client.get('/')
    #     self.assertContains(response, '1-title')
    #     self.assertContains(response, '1-body')
    #
    # def test_two_entries(self):
    #     Cv.objects.create(title='1-title', body='1-body')
    #     Cv.objects.create(title='2-title', body='2-body')
    #     response = self.client.get('/')
    #     self.assertContains(response, '1-title')
    #     self.assertContains(response, '1-body')
    #     self.assertContains(response, '2-title')
    def test_no_entries(self):
    response = self.client.get('/')
    self.assertContains(response, 'No blog entries yet.')
