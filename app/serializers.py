from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from app.models import Test, Answer, Question, Lesson, Chapter, TestUser, LessonUser, Dictionary, Word


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
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        try:
            lesson_user = LessonUser.objects.get(user=self.context['request'].user, lesson=instance)
            status = lesson_user.status
        except LessonUser.DoesNotExist:
            status = None
        ret['status'] = status
        return ret


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(source='answer_set', many=True)

    class Meta:
        model = Question
        exclude = ('test',)


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(source='question_set', many=True)

    class Meta:
        model = Test
        fields = '__all__'


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = '__all__'


class DictionarySerializer(serializers.ModelSerializer):
    words = WordSerializer(source='word_set', many=True)

    class Meta:
        model = Dictionary
        fields = '__all__'