from django.test import TestCase

from cv.models import Cv_section

class CvSectionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Cv_section.objects.create(title='title1', text='this is sample text1')
        Cv_section.objects.create(title='title1', text='this is sample text1')
        # self.cv_section_new_url=reverse('cv_section_new')

    def test_title_name_label(self):
        cv_section = Cv_section.objects.get(id=1)
        title_label = cv_section._meta.get_field('title').verbose_name
        self.assertEquals(title_label, 'title')

    def test_text_name_label(self):
        cv_section = Cv_section.objects.get(id=1)
        text_label = cv_section._meta.get_field('text').verbose_name
        self.assertEquals(text_label, 'text')

    def test_title_max_length(self):
        cv_section = Cv_section.objects.get(id=1)
        max_length = cv_section._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)
    # def test_displays_all_cv_sections(self):
    #     # Cv_section.objects.create(title='title 1')
    #
    #
    #     response = self.client.get('/cv')
    #     print(response)
    #     self.assertIn('title1', response.content.decode())
    #     self.assertIn('title2', response.content.decode())
    def test_model_creation_representation(self):
        cv_section_one= Cv_section(title="title_one",text="this is my text one")
        cv_section_two= Cv_section(title="title_two",text="this is my text two")

        self.assertEqual("title_one",cv_section_one.title)
        self.assertEqual("title_two",cv_section_two.title)
        self.assertEqual("this is my text one",cv_section_one.text)
        self.assertEqual("this is my text two",cv_section_two.text)
