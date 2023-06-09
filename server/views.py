from django.shortcuts import render
from .forms import *
from .utils import *


def upload_file(request):
    if request.method == 'POST':
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            file = handle_file(request.FILES['file'])
            return render(request, 'server/result.html', {'file': file})
    else:
        form = UploadFile()

    return render(request, 'server/upload.html', {'form': form})
