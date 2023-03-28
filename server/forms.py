from django import forms
from .models import *


class UploadFile(forms.Form):
    file = forms.FileField()

    class Meta:
        model = FileField
        fields = ['file']
