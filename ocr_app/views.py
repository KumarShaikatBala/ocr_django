from django.shortcuts import render, redirect, get_object_or_404
from .forms import DocumentForm
from .models import Document
from .utils import process_document

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            process_document(document)
            return redirect('document_detail', doc_id=document.id)
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})

def upload_success(request):
    return render(request, 'success.html')

def document_detail(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    return render(request, 'document_detail.html', {'document': document})