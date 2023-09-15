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


class PostUpdateSerializer(serializers.Serializer):
    
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    
    class Meta:
        model = Post
        fields = ('title', 'content')

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title),
        instance.content = validated_data.get('content', instance.content),
        instance.save()
        return instance
