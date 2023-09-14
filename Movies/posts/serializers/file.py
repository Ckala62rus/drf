from datetime import datetime

from rest_framework import serializers

from posts.models.post_file import PostFile


class FileSerializer(serializers.ModelSerializer):

    created_at = serializers.SerializerMethodField()

    class Meta:
        model = PostFile
        # fields = '__all__'
        exclude = ('post',)


    def get_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")
