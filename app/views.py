from numbers import Number

from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework.decorators import permission_classes, action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from app.models import Test, Lesson
from app.serializers import RegisterSerializer, Test1Serializer, UsersSerializer, LessonsSerializer, LessonSerializer


class TestsViewSet(ModelViewSet):
    serializer_class = Test1Serializer
    queryset = Test.objects.all()


class RegisterView(mixins.CreateModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UsersView(mixins.ListModelMixin, GenericViewSet):
    pagination_class = PageNumberPagination
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class LessonsView(mixins.ListModelMixin, GenericViewSet):
    pagination_class = PageNumberPagination
    queryset = Lesson.objects.all()
    serializer_class = LessonsSerializer


class LessonView(mixins.ListModelMixin, GenericViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
