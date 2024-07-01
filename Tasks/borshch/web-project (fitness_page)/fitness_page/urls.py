"""
URL configuration for fitness_page project.

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
import nastya.views as nastya_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_page/', nastya_views.main_page),
    path('', nastya_views.main_page, name="main_page"),
    path('consultations/', nastya_views.consultations, name="consultations"),
    path('courses/', nastya_views.courses, name="courses"),
    path('courses/morning/', nastya_views.morning, name="morning"),
    path('courses/lite/', nastya_views.lite, name="lite"),
    path('courses/pro/', nastya_views.pro, name="pro"),
    path('courses/individual/', nastya_views.individual, name="individual"),
    path('courses/camp/', nastya_views.camp, name="camp"),
    path('maintenance/', nastya_views.maintenance, name="maintenance"),
    path('manual/', nastya_views.manual, name="manual"),
    path('about_me/', nastya_views.about_me, name="info"),
    path('poll/', nastya_views.poll, name="poll")

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
