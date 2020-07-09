from django import forms

from .models import Cv_section

class Cv_section_form(forms.ModelForm):

    class Meta:
        model = Cv_section
        fields = ('title', 'text',)
