"""cleverbots URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from main.api.views import ImagesAPIViewSet


urlpatterns = [
    path('api/image/', ImagesAPIViewSet.as_view({'post': 'create'}), name='post_image'),
    path('api/images/', ImagesAPIViewSet.as_view({'get': 'list'}), name='get_images'),
    path('admin/', admin.site.urls),
]
