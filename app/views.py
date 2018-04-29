from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import mixins
from rest_framework.decorators import api_view, detail_route, action
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from app.models import Test, Lesson, TestUser, LessonUser, Dictionary
from app.serializers import RegisterSerializer, TestSerializer, UsersSerializer, LessonsSerializer, TestUserSerializer, \
    LessonUserSerializer


class RegisterView(mixins.CreateModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UsersView(mixins.ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class LessonsView(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonsSerializer

    def get_queryset(self):
        if self.request.GET.get('my') is not None:
            return Lesson.objects.filter(lessonuser__user=self.request.user)
        else:
            return Lesson.objects.all()

    @action(detail=True, methods=['post'], url_path='start')
    def start_lesson(self, request, pk=None):
        lesson = self.get_object()
        LessonUser.objects.create(lesson=lesson, user=request.user)
        return Response()

    @action(detail=True, methods=['post'], url_path='stop')
    def stop_lesson(self, request, pk=None):
        lesson = self.get_object()
        lesson_user = LessonUser.objects.get(lesson=lesson, user=request.user)
        lesson_user.status = 1
        lesson_user.save()
        return Response()


class TestsViewSet(ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()

    def get_queryset(self):
        if self.request.GET.get('my') is not None:
            return Test.objects.filter(testuser__user=self.request.user)
        else:
            return Test.objects.all()


def get_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    user = request.user
    return test, user


class TestUserViewSet(ModelViewSet):
    queryset = TestUser.objects.all()
    serializer_class = TestUserSerializer

    def create(self, request):
        data = request.data
        test_id = data.get('test_id')
        if test_id is None:
            raise ValidationError(dict(test_id='This field is required'))
        test, user = get_test(request, test_id)

        print(user)
        TestUser.objects.create(user=user, test=test)
        return Response()


class LessonUserViewSet(ModelViewSet):
    queryset = LessonUser.objects.all()
    serializer_class = LessonUserSerializer

