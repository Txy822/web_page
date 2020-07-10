from django.test import TestCase,Client
from django.urls import reverse
from cv.models import Cv_section



class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
        self.cv_section_list_url=reverse('cv_section_list')
        self.cv_section_detail_url=reverse('cv_section_detail',args=[1])
        self.cv_section_new_url=reverse('cv_section_new')
        self.cv_section_edit_url=reverse('cv_section_edit',args=[1])
        self.cv_section_remove_url=reverse('cv_section_remove',args=[1])


    def test_cv_section_list_GET(self):
        response=self.client.get(self.cv_section_list_url)
        self.assertEquals(response.status_code,200)
        print(response)
        self.assertTemplateUsed(response,'cv/cv_section_list.html')
        
    def test_cv_section_detail_GET(self):
        response=self.client.get(self.cv_section_detail_url)
        self.assertEquals(response.status_code,404)
        print(response)
        #self.assertTemplateUsed(response,'cv/cv_section_detail.html')

    def test_cv_section_new_GET(self):
        response=self.client.get(self.cv_section_new_url)
        self.assertEquals(response.status_code,200)

    def test_cv_section_edit_GET(self):
        response=self.client.get(self.cv_section_edit_url)
        self.assertEquals(response.status_code,404)
        print(response)
        #self.assertTemplateUsed(response,'cv/cv_section_edit.html')

    def test_cv_section_remove_GET(self):
        response=self.client.get(self.cv_section_remove_url)
        self.assertEquals(response.status_code,404)
        print(response)





# from django.test import TestCase
#
# # Create your tests here.
# from cv.models import Cv_section
# from django.urls import resolve
# from django.test import TestCase
# from django.http import HttpRequest
#
# from cv.views import cv_section_list
#
#
# # Another Test: Entrys
# #
# # Did you notice that the pluralization of cv is misspelled in the admin interface? “cvs” should instead read “cvies”.
# # Let’s write a test to verify that when Django correctly pluralizes “cv” to “cvies”.
# class cv_section_model_test(TestCase):
#     def test_cv_url_resolves_to_cv_page_view(self):
#         found = resolve('/cv/')
#         self.assertEqual(found.func, cv_section_list)
#     def test_cv_page_returns_correct_html(self):
#         request = HttpRequest()
#         response = cv_section_list(request)
#         html = response.content.decode('utf8')
#         #self.assertTrue(html.startswith('<html>'))
#         self.assertIn('<title>Tesfahun Curriculum Vitae</title>', html)
#         #self.assertTrue(html.endswith('</html>'))
#     def test_title_str_representation(self):
#         tit= Cv_section(title="mytitle")
#         self.assertEqual(str(tit),tit.title)
#     # def test_text_representation(self):
#     #     tex= Cv(text="this is my text")
#     #     self.assertEqual("this is my text",tex.text)
#     def test_verbose_name_plural(self):
#         #self.assertEqual(str(Cv._meta.verbose_name_plural), "cvs")
#         self.assertEqual(str(Cv_section._meta.verbose_name_plural), "cv_sections")
#
# #         Every site should have a homepage. Let’s write a failing test for that.
# #
# # We can use the Django test client to create a test to make sure
# # that our homepage returns an HTTP 200 status code (this is the standard response for a successful HTTP request).
#     def  test_homepage(self):
#         response=self.client.get('/')
#         self.assertEqual(response.status_code,200)
#
#     # def test_one_entry(self):
#     #     Cv.objects.create(title='1-title', text='1-body')
#     #     response = self.client.get('/')
#     #     self.assertContains(response, '1-title')
#     #     self.assertContains(response, '1-body')
#     #
#     # def test_two_entries(self):
#     #     Cv.objects.create(title='1-title', body='1-body')
#     #     Cv.objects.create(title='2-title', body='2-body')
#     #     response = self.client.get('/')
#     #     self.assertContains(response, '1-title')
#     #     self.assertContains(response, '1-body')
#     #     self.assertContains(response, '2-title')
#     # def test_no_entries(self):
#     # response = self.client.get('/')
#     # self.assertContains(response, 'No blog entries yet.')
#
#
#
#
#
# # from django.test import TestCase
# #
# # # Create your tests here.
# # from .models import Cv
# #
# #
# # # Another Test: Entrys
# # #
# # # Did you notice that the pluralization of cv is misspelled in the admin interface? “cvs” should instead read “cvies”.
# # # Let’s write a test to verify that when Django correctly pluralizes “cv” to “cvies”.
# # class CvModelTest(TestCase):
# #     def test_title_str_representation(self):
# #         tit= Cv(title="mytitle")
# #         self.assertEqual(str(tit),tit.title)
# #     # def test_text_representation(self):
# #     #     tex= Cv(text="this is my text")
# #     #     self.assertEqual("this is my text",tex.text)
# #     def test_verbose_name_plural(self):
# #         #self.assertEqual(str(Cv._meta.verbose_name_plural), "cvs")
# #         self.assertEqual(str(Cv._meta.verbose_name_plural), "cvies")
# #
# # #         Every site should have a homepage. Let’s write a failing test for that.
# # #
# # # We can use the Django test client to create a test to make sure
# # # that our homepage returns an HTTP 200 status code (this is the standard response for a successful HTTP request).
# #     def  test_homepage(self):
# #         response=self.client.get('/')
# #         self.assertEqual(response.status_code,200)
# #
# #     # def test_one_entry(self):
# #     #     Cv.objects.create(title='1-title', text='1-body')
# #     #     response = self.client.get('/')
# #     #     self.assertContains(response, '1-title')
# #     #     self.assertContains(response, '1-body')
# #     #
# #     # def test_two_entries(self):
# #     #     Cv.objects.create(title='1-title', body='1-body')
# #     #     Cv.objects.create(title='2-title', body='2-body')
# #     #     response = self.client.get('/')
# #     #     self.assertContains(response, '1-title')
# #     #     self.assertContains(response, '1-body')
# #     #     self.assertContains(response, '2-title')
# #     def test_no_entries(self):
# #     response = self.client.get('/')
# #     self.assertContains(response, 'No blog entries yet.')
