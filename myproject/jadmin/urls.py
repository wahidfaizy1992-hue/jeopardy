from django.urls import path
from . import views

app_name="jadmin"

urlpatterns = [
    path('', views.homepage),
]