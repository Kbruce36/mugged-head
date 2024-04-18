from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index , name='index'),
    path('pricing', views.pricing, name='pricing'),
    path('about', views.about, name = 'about'),
    
]