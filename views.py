from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
from .utils import process_document

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            process_document(document)
            return redirect('upload_success')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})

def upload_success(request):
    return render(request, 'success.html')