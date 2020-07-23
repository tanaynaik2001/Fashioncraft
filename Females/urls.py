from django.urls import path
from . import views

urlpatterns = [
    path('females', views.females, name='females'),
]