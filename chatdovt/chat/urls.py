from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define a página inicial do chat
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('policie/', views.policie, name='policie'),
]