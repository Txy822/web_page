from django.test import TestCase,Client
from django.test import TestCase

from django.urls import reverse,resolve
from cv.views import cv_section_list,cv_section_detail,cv_section_new,cv_section_edit,cv_section_remove
from cv.models import Cv_section

class UnitTest_template(TestCase):

    def setUp(self)

        self.client=Client()

    def test_homepage_template(self):
        
        #cv_section_list_url=reverse('cv/cv_section_list/')
        #response=self.client.get('/')
        response=self.client.get('/cv/')
        self.assertTemplateused(response,'cv_sections','cv/cv_section_list.html')
