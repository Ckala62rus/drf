from rest_framework import serializers

from posts.models.post import Post
from posts.serializers.file import FileSerializer


class PostGetSerializer(serializers.ModelSerializer):

    files = FileSerializer(many=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'is_publish',
            'created_at',
            'updated_at',
            'files',
        )
        depth = 1

