"""
URL configuration for crudapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# crudapp/urls.py

from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.create, name='create'),
    path('read/', views.read, name='read'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]

# myproject/urls.py


# myproject/urls.py







# crudapp/urls.py

