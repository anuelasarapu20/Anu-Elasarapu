from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_image

urlpatterns = [
  path('upload/', upload_image, name='upload_image'),
]