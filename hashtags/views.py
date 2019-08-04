from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Hashtag, SearchTask
from .serializers import HashtagSerializer, SearchTaskSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated


class SearchTaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = SearchTask.objects.all()
    pagination_class = LimitOffsetPagination
    serializer_class = SearchTaskSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('status', )
    ordering_fields = ('updated_at', )
    ordering = ('updated_at', )
    
    def perform_create(self, serializer):
        tag_serializer = HashtagSerializer(data=self.request.data['hashtag'])
        tag_serializer.is_valid()
        tag_serializer.save()
        serializer.is_valid()
        task = serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

class SearchTaskFilterViewSet(generics.ListAPIView):
    serializer_class = SearchTaskSerializer
    def get_queryset(self):
        query_hashtag = self.kwargs['hashtag']
        return SearchTask.objects.filter(hashtag__name=query_hashtag)