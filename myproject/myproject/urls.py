"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from . import views
# from django.conf.urls.static import static
# from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home_view'),
    path('about/', views.about),
    path('rules/', views.rules),
    path('host/', views.host),
    path('start/', views.start),
    path('new_category/', views.new_category),
    path('wel_test/', views.wel_test),
    path('clue/<str:clue_key>/', views.get_clue_detail, name='get_clue'),
    path('names/', views.get_player_names, name='get_names'),
    path('jadmin/', include('jadmin.urls'))
  
]

