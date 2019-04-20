from rest_framework import serializers
from main.models import Image


class ImagesSerializer(serializers.ModelSerializer):
    date = serializers.DateField(source='create_date')
    path_to_img = serializers.CharField(source='content')
    size = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ('id', 'date', 'place', 'path_to_img', 'size')

    def get_size(self, obj):
        return obj.content.size


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('content', 'place')

