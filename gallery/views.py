from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Photo 
from .forms import PhotoUploadForm

def photo_list(request):
    photos = Photo.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery/photo_list.html', {'photos': photos})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'gallery/photo_detail.html', {'photo': photo})

@login_required
def photo_upload(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('gallery:photo_detail', pk=photo.pk)
    else:
        form = PhotoUploadForm()
    return render(request, 'gallery/photo_upload.html', {'form': form})

@login_required
def like_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.user in photo.likes.all():
        photo.likes.remove(request.user)
        liked = False
    else:
        photo.likes.add(request.user)
        liked = True
    return JsonResponse({'liked': liked, 'total_likes': photo.total_likes()})


