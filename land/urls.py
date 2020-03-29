from django.urls import path

from land import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('documents', views.documents, name='documents'),
    path('services', views.services, name='services'),
]
