"""
URL configuration for UrbanDjango project.

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
from tempfile import template


from django.contrib import admin
from django.urls import path
from task5.views import sign_up_by_html, sign_up_by_django
from task4.views import platform_templates,games_templates,cart_templates

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", platform_templates),
    path("games/",games_templates),
    path("cart/", cart_templates),
    path("req/", sign_up_by_html),
    path("for/", sign_up_by_django),
]
#
# cd UrbanDjango
# python manage.py runserver

# python manage.py makemigrations
# python manage.py migrate