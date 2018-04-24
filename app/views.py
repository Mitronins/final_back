from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import View
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import ValidationError, ParseError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from app.models import Test, Lesson, Question
from app.serializers import TestsSerializer, UserSerializer, TestSerializer, QuestionSerializer, AnswerSerializer, \
    Test1Serializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class NoCSRFView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication,)


class TestsView(NoCSRFView):
    def get(self, request):
        tests = Test.objects.all()

        return Response(data={
            'data': TestsSerializer(tests, many=True).data
        })


class TestView(NoCSRFView):
    def get(self, request, test_id):
        test = Test.objects.prefetch_related('question_set__answer_set').get(id=test_id)
        print(test.question_set.all()[1].answer_set.all())
        questions = test.question_set.all()

        data_json = TestSerializer(test).data
        data_json['questions'] = QuestionSerializer(questions, many=True).data

        count = 0
        for ques in data_json['questions']:
            data_json['questions'][count]['answers'] = AnswerSerializer(test.question_set.all()[count].answer_set.all(),
                                                                        many=True).data
            count += 1
        return Response(data={
            'data': data_json
        })


class TestViewSet(ModelViewSet):
    serializer_class = Test1Serializer
    queryset = Test.objects.all()


class LessonsView(NoCSRFView):
    def get(self, request):
        lessons = Lesson.objects.all()

        return Response(data={
            'data': TestSerializer(lessons, many=True).data
        })


class LessonView(NoCSRFView):
    def get(self, request):
        lessons = Lesson.objects.all()

        return Response(data={
            'data': TestSerializer(lessons, many=True).data
        })


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LoginView(NoCSRFView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        user = User.objects.get(username=username)
        if username and password:
            login(request, user)
            return Response()


class RegisterView(NoCSRFView):

    def post(self, request):
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        username = request.data.get('username')
        password = request.data.get('password')
        if username and password and first_name:
            try:
                user = User.objects.get(username=username)
                raise ValidationError(detail='Username not unique')
            except User.DoesNotExist:
                user = User(
                    email=email,
                    first_name=first_name,
                    password=make_password(password)
                ).save()
                user = User.objects.get(username=username)
                userializer = UserSerializer(user)
                # token = generate_token(email=email, password=password, user_id=user.id)
                user = userializer.data
                return Response(
                    data={
                        'user': user
                    })
        else:
            raise ParseError
