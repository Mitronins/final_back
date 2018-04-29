from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from app.models import Test, Answer, Question, Lesson, Chapter, TestUser, LessonUser, Dictionary


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)
        user = User.objects.create(**validated_data)
        Dictionary.objects.create(user=user)
        return user


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        exclude = ('lesson',)


class LessonsSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(source='chapter_set', many=True)

    class Meta:
        model = Lesson
        fields = ('id', 'title', 'description', 'chapters')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(source='answer_set', many=True)

    class Meta:
        model = Question
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(source='question_set', many=True)

    class Meta:
        model = Test
        fields = '__all__'


class TestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestUser
        fields = '__all__'


class LessonUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonUser
        fields = '__all__'
