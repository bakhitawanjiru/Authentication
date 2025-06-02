from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('photo/upload/', views.photo_upload, name='photo_upload'),
    path('photo/<int:pk>/like/', views.like_photo, name='like_photo'),
]