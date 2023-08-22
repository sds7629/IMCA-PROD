from rest_framework import serializers

from .models import CommonModel


class CommonModelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")  # 년-월-일 시:분 형식으로 변환
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = CommonModel
        fields = "__all__"
