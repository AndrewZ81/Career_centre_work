from rest_framework import serializers

from .models import Company


class CompanyCreateSerializer(serializers.ModelSerializer):
    """Создаёт участника торговой сети."""
    class Meta:
        model = Company
        read_only_fields = ('id', 'created')
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    """
    Отображает список участников торговой сети.
    Для запрашиваемого участника торговой сети:
    - выводит подробную информацию.
    - редактирует содержимое.
    - удаляет.
    """
    class Meta:
        model = Company
        read_only_fields = ('id', 'created', 'debt')
        fields = '__all__'
