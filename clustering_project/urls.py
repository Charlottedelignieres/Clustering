"""
URL configuration for clustering_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from results import views_exploration 
from django.conf import settings
from django.conf.urls.static import static
from results import views_clustering

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exploration/', views_exploration.exploration_page, name='exploration_page'),
    path('clustering/', views_clustering.clustering_page, name='clustering_page')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)