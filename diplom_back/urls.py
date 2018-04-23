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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from app.views import TestView, LoginView, UserView, TestsView

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', TestView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    url(r'test/(?P<test_id>[0-9]+)/$', TestView.as_view()),
    url(r'tests/', TestsView.as_view()),
]

# urlpatterns = {
#     url('admin/', admin.site.urls),
#     url('login/', LoginView.as_view()),
#     url('user/', UserView.as_view()),
#     url('register/', RegisterView.as_view()),
#     url('tests/', TestsView.as_view()),
#     url('lessons/', LessonsView.as_view()),
#     url('lesson/', LessonView.as_view()),
#
