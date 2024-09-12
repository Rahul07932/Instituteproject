"""
URL configuration for Instituteproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Instituteapp import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.loginpage,name='login'),
    path('register/',views.registrationForm,name='register'),
    path('login/',views.loginpage,name='login'),
     path('logout/',views.logoutpage,name='logout'),
     path('contact/',views.contact,name='contact'),
    path('gallery/',views.gallery,name='gallery'),
    path('service/',views.service,name='service'),
    path('feedback/',views.feedback,name='feedback'),
    path('home/',views.home,name='home'),
    path('enroll/<id>',views.enroll,name='enroll'),
]
