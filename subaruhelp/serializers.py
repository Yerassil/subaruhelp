from rest_framework import serializers

from .models import ObdCode, Comment


class ObdCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObdCode
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
