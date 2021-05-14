"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import hello.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello.views.home, name='home'),
    path('vigenere_input/', hello.views.vigenere_input, name='vigenere_input'),
    path('vigenere/', hello.views.vigenere_encrypt, name='vigenere'),
    path('caesar/', hello.views.caesar, name='caesar'),
    path('subst_input/', hello.views.subst_input, name='subst_input'),
    path('subst_cioutput/', hello.views.subst_encrypt, name='subst_cioutput'),
    path('subst_ploutput/', hello.views.subst_decrypt, name='subst_ploutput'),
]
