from django.contrib import admin
from django.urls import path, include
from Jandusayapp import views  # Import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('Jandusayapp.urls')),  # Include your app's URLs
    path('', views.home, name='home'),  # Root path that goes to the home view
]
