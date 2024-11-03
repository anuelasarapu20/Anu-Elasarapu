from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from . models import ImageUpload
from . utils import imagetext
import os

def upload_image(request):
  if request.method == 'POST':
    form = ImageUploadForm(request.POST, request.FILES)
    print(form.is_valid());
    if form.is_valid():
      image_instance = form.save() # Save the form and get the ImageUpload instance
      file_path = image_instance.image.path
      print(file_path);
      arr = imagetext(file_path);

      values = {
        'img': image_instance.image.url,
        'name':arr[0], 
        'dob':arr[1], 
        'father_name':arr[2],
        'type':arr[3]
      }

      return render(request, 'upload.html', values) # Redirect to a success page or the same page
    else:
      print(form.errors)
  else:
    form = ImageUploadForm()
  return render(request, 'upload.html', {'form': form})
