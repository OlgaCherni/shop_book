"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from discovery import views as dis
from django.conf.urls.static import static                         # 2(5)шаг для отображения на странице картинок из базы данных
from django.conf import settings                                   # 3(5)шаг для отображения на странице картинок из базы данных

urlpatterns = [
    path('admin/', admin.site.urls),                               # Стандарный путь! 
    path("", dis.index, name="index"),                             # Регистрация (суф/ прил(или views).функция1(из вьюс), +-name="..."в пути(обычно как html файл) )
    path("reg/", dis.reg, name="reg"),                             # Без регистрации
    path("product/<int:book_id>", dis.product, name="prod"),       # Один продукт
    path("store/", dis.store_catalog, name="catalog"),             # Каталог
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # 4(5)шаг для отображения на странице картинок из базы данных
