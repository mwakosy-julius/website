from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('products', views.products, name='products'),
    path('blog', views.blog, name='blog'),
    path('contacts', views.contacts, name='contacts'),
]
