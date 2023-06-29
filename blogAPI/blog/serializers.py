from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "author", "body"]

    def to_representation(self, instance):
        return {
            "id" : instance.id,
            "title" : instance.title,
            "author" : instance.author,
            "body" : instance.body,
            "created_at" : instance.created_at
        }