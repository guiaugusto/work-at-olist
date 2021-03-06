"""libstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.urls import include
from django.conf.urls import url
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from authors import urls as authors_urls
from books import urls as books_urls

router = DefaultRouter()

router.registry.extend(authors_urls.router.registry)
router.registry.extend(books_urls.router.registry)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', include(router.urls))
]
