from django import forms

from .models import Cv

class CvForm(forms.ModelForm):

    class Meta:
        model = Cv
        fields = ('title', 'text',)
