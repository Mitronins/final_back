from rest_framework import serializers


class TestSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(max_length=550, required=True)

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=255, required=True)
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
