from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Hashtag, CoOccurrence, Biterm
from .serializers import HashtagSerializer, CoOccurrenceSerializer, BitermSerializer, WordSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated


class BitermViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Biterm.objects.all()
    serializer_class = BitermSerializer

    def perform_create(self, serializer):
        word_i_serializer = WordSerializer(data=self.request.data['word_i'])
        word_i_serializer.is_valid()
        word_i_serializer.save()
        word_j_serializer = WordSerializer(data=self.request.data['word_j'])
        word_j_serializer.is_valid()
        word_j_serializer.save()
        coOccurrence = serializer.save()


class CoOccurrenceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = CoOccurrence.objects.all()
    serializer_class = CoOccurrenceSerializer

    def perform_create(self, serializer):
        word_i_serializer = WordSerializer(
            data=self.request.data['biterm']['word_i'])
        word_i_serializer.is_valid()
        word_i_serializer.save()
        word_j_serializer = WordSerializer(
            data=self.request.data['biterm']['word_j'])
        word_j_serializer.is_valid()
        word_j_serializer.save()
        tag_serializer = HashtagSerializer(data=self.request.data['hashtag'])
        tag_serializer.is_valid()
        tag_serializer.save()
        biterm_serializer = BitermSerializer(data=self.request.data['biterm'])
        biterm_serializer.is_valid()
        biterm_serializer.save()
        coOccurrence = serializer.save()
