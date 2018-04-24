from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from app.models import Test, Answer, Question


class TestsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(max_length=550, required=True)


class TestSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(max_length=550, required=True)
    # questions = QuestionSer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

    # answers


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(source='answer_set', many=True)

    class Meta:
        model = Question
        fields = '__all__'
    # answers


class Test1Serializer(serializers.ModelSerializer):
    questions = QuestionSerializer(source='question_set', many=True)

    class Meta:
        model = Test
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)
        return User.objects.create(**validated_data)

# class AnswerSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     text = serializers.CharField(max_length=255, required=True)
#     is_true = serializers.BooleanField()
#
#
# class CompanySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=1000, required=True)
#     link = serializers.CharField(max_length=1000, required=True)
#     description = serializers.CharField(max_length=1000, required=True)
#     phone = serializers.CharField(max_length=1000, required=True)
#     housing = serializers.IntegerField(required=False)
#     pavilion = serializers.CharField(max_length=1000, required=True)
#     floor = serializers.IntegerField(required=False)
#     tags = serializers.SerializerMethodField('get_tagslist')
#
#     def get_tagslist(self, obj):
#         tags = obj.tags.all()
#         return ProductServiceSerializer(tags, many=True).data
#
#
# class LeaseSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     main_photo = serializers.SerializerMethodField('get_mediaphoto')
#     square = serializers.FloatField(required=True)
#     cost = serializers.IntegerField(required=True)
#     floor = serializers.IntegerField(required=True)
#     housing = serializers.IntegerField(required=False)
#     function = serializers.CharField(max_length=255, required=True)
#     show = serializers.BooleanField()
#     order = serializers.IntegerField(required=False)
#     photos = serializers.SerializerMethodField('get_mediaphotos')
#
#     def get_mediaphoto(self, obj):
#         if obj.main_photo:
#             return obj.main_photo.url
#         return None
#
#     def get_mediaphotos(self, obj):
#         photos = Photo.objects.filter(lease=obj)
#         if len(photos) > 0:
#             photos = [ph.photo.url for ph in photos]
#             return photos
#         else:
#             return []
