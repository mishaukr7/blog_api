from .models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        allow_null=False,
        default=serializers.CurrentUserDefault(),
        read_only=True
    )

    def validate_user(self, value):
        return self.context['request'].user

    class Meta:
        model = Article
        fields = ('id', 'user', 'name', 'created', 'content',)
