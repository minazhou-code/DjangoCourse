"""MyCourses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('about/', TemplateView.as_view(template_name="about.html")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('Blogs/', include('Blogs.urls')),
    path('user/', include('UserAdmin.urls')),
    path('Courses/', include('Courses.urls')),
    path('Student/', include('Student.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), # New entry
    path('api/', include('Courses.API.urls')), # New entry
    path('api/', include('Blogs.API.urls')), # New entry
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
