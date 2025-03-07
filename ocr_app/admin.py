from django.contrib import admin
from .models import Document
from .utils import process_document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'uploaded_at', 'status', 'text')
    actions = ['process_selected']

    def process_selected(self, request, queryset):
        for document in queryset:
            process_document(document)
        self.message_user(request, "Processing started for selected documents")

    process_selected.short_description = "Process selected documents"

    # Automatically run OCR when saving via admin
    def save_model(self, request, obj, form, change):
        if obj.file and not obj.text:
            process_document(obj)
        super().save_model(request, obj, form, change)
