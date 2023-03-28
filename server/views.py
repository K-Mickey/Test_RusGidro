from django.shortcuts import render
from django.views.generic import FormView
from .forms import *


class UploadFile(FormView):
    form_class = UploadFile
    template_name = 'server/upload.html'

