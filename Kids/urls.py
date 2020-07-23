from django.urls import path
from . import views

urlpatterns = [
    path('kids', views.kids, name='kids'),
]