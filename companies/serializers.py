from rest_framework import serializers

from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    """Создаёт участника торговой сети"""

    class Meta:
        model = Company
        read_only_fields = ("id", "created")
        fields = "__all__"
