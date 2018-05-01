from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from app.models import Test, Lesson, TestUser, LessonUser, Dictionary, Word
from app.serializers import RegisterSerializer, TestSerializer, UsersSerializer, LessonsSerializer, \
    DictionarySerializer, WordSerializer


class RegisterView(mixins.CreateModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UsersView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class LessonsView(ModelViewSet):
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

    def get_queryset(self):
        if self.request.GET.get('my') is not None:
            return Test.objects.filter(testuser__user=self.request.user)
        else:
            return Test.objects.all()

    @action(detail=True, methods=['post'], url_path='start')
    def start_test(self, request, pk=None):
        test = self.get_object()
        TestUser.objects.create(test=test, user=request.user)
        return Response()

    @action(detail=True, methods=['post'], url_path='stop')
    def stop_test(self, request, pk=None):
        right_answers = request.data.get('right_answers')
        if right_answers is None:
            raise ValidationError(dict(right_answers='This field is required'))
        test = self.get_object()
        test_user = TestUser.objects.get(test=test, user=request.user)
        test_user.status = 1
        test_user.right_answers = right_answers
        test_user.save()
        return Response()


class DictionaryViewSet(ModelViewSet):
    pagination_class = None
    serializer_class = DictionarySerializer

    def get_queryset(self):
        if self.request.user is not None:
            dictionary = Dictionary.objects.filter(user=self.request.user)
            return dictionary
        else:
            return Test.objects.all()

    @action(detail=True, methods=['post'], url_path='add')
    def add_word(self, request, pk=None):
        data = request.data
        data['dictionary'] = pk
        word = WordSerializer(data=data)
        word.is_valid(raise_exception=True)
        print(word.validated_data)
        word.save()
        return Response()

    @action(detail=True, methods=['post'], url_path='delete')
    def delete_word(self, request, pk=None):
        id_word = request.data.get('id_word')
        word = Word.objects.get(id=id_word)
        word.delete()
        return Response()
