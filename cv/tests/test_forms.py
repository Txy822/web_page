from django.test import TestCase

from cv.forms import Cv_section_form

class CvSectionFormTest(TestCase):

    def test_cv_section_form_valid_data(self):
        form =Cv_section_form(data={
        'title' : 'Form Title',
        'text' : 'this is my form text'
        })

        self.assertTrue(form.is_valid())

    def test_cv_section_form_no_data(self):
        form=Cv_section_form(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),2)
