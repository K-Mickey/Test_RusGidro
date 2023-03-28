from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from .utils import *


def upload_file(request):
    if request.method == 'POST':
        print('YES')
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            handle_file(request.FILES['file'])
            return render(request, 'server/result.html')
    else:
        form = UploadFile()

    return render(request, 'server/upload.html', {'form': form})
