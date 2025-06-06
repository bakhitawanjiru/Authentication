"""
URL configuration for authproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as django_auth_views  # Rename this import
from authapp import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authapp.urls')),
    path('', include('gallery.urls')),
    path('register/', auth_views.register, name='register'),
    
    # Use django's built-in auth views
    path('login/', django_auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', django_auth_views.LogoutView.as_view(next_page='gallery:photo_list'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
