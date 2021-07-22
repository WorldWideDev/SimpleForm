from django import forms
from main.models import Sample

class SampleForm(forms.ModelForm):
    
    class Meta:
        fields = '__all__'
        model = Sample