"""diplom_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.utils import AuthToken
from app.views import TestsViewSet, RegisterView, UsersView, LessonsView, DictionaryViewSet

router = DefaultRouter()
router.register('tests', TestsViewSet, base_name='tests')
router.register('register', RegisterView, base_name='register')
router.register('users', UsersView, base_name='users')
router.register('lessons', LessonsView, base_name='lessons')
router.register('dictionary', DictionaryViewSet, base_name='dictionary')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', AuthToken.as_view()),
]
