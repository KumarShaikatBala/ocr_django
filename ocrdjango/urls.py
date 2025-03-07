from django.contrib import admin
from django.urls import path
from ocr_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.upload_document, name='upload'),
    path('success/', views.upload_success, name='upload_success'),
    path('document/<int:doc_id>/', views.document_detail, name='document_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)