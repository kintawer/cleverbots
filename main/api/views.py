from rest_framework import viewsets
from rest_framework.views import Response
from django_filters import rest_framework as filters

from main.api.serializers import ImageSerializer, ImagesSerializer
from main.api.filters import ImagesFilter
from main.models import Image


class ImagesAPIViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImagesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ImagesFilter

    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        return Response(status=400)

