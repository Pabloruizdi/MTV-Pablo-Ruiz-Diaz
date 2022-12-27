"""entregable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from entregable.views import familiar_1, familiar_2, fechahoy, vistatemplate, index
from fam.views import creacionfamiliar, lista_fam

urlpatterns = [
    path("",index, name="inicio"),
    path('admin/', admin.site.urls),
    path("Creacionfamiliar/", creacionfamiliar),
    path("ListaFamiliares/", lista_fam),
    path("Vistatemplate/", vistatemplate),
]
