# Jandusayapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page showing all posts
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),  # Post detail view
]
