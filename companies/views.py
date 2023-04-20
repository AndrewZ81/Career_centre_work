from rest_framework import generics, permissions, filters
from rest_framework.serializers import Serializer
from django_filters.rest_framework import DjangoFilterBackend


from .serializers import CompanySerializer, CompanyCreateSerializer
from .models import Company


class CompanyCreateView(generics.CreateAPIView):
    """Обрабатывает запрос на создание участника торговой сети."""
    permission_classes: list = [permissions.IsAuthenticated]
    serializer_class: Serializer = CompanyCreateSerializer


class CompanyListView(generics.ListAPIView):
    """
    Обрабатывает запрос на отображение списка участников торговой сети.
    Поддерживает сортировку и поиск по названию, а также фильтрацию по городу.
    """
    queryset = Company.objects.all()
    permission_classes: list = [permissions.IsAuthenticated]
    serializer_class: Serializer = CompanySerializer

    filter_backends: list = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_fields: list = ['town']
    search_fields: list = ['title']
    ordering_fields: list = ['title']
    ordering: str = 'title'


class CompanyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Для запрашиваемого участника торговой сети:
    - выводит подробную информацию.
    - редактирует содержимое.
    - удаляет.
    """
    queryset = Company.objects.all()
    serializer_class: Serializer = CompanySerializer
    permission_classes: list = [permissions.IsAuthenticated]
