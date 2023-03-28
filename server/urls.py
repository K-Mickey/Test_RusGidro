from django.urls import path
from .views import *

urlpatterns = [
    path('', UploadFile.as_view(), name='home'),
    ]
