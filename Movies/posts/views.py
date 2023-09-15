from django.shortcuts import render
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models.post import Post
from posts.serializers.post import PostGetSerializer, PostUpdateSerializer


# Create your views here.


# @api_view(['GET'])
# def GetPosts(request):
#     posts = Post.objects.all().values()
#     serializer = PostGetSerializer(posts, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#     # return Response(posts)


@extend_schema_view(
        get=extend_schema(
            summary='Все посты',
            tags=['Посты'],
        ),
    )
class PostsView(APIView):

    permission_classes = [IsAuthenticated]

    """Get all posts"""
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostGetSerializer(posts, many=True)
        return Response(serializer.data)


@extend_schema_view(
        delete=extend_schema(
            summary='Удалить пост',
            tags=['Посты'],
        ),
    )
class PostsDeleteView(APIView):
    def delete(self, request, id):
        try:
            post = Post.objects.get(pk=id)
            post.delete()
            return Response(f'delete post with id:{id} was deleted')
        except Exception:
            return Response(f'post with id:{id} not found', status=status.HTTP_404_NOT_FOUND)


@extend_schema_view(
        put=extend_schema(
            summary='Обновить пост',
            tags=['Посты'],
            request=PostUpdateSerializer
        ),
    )
class PostsUpdateView(APIView):
    def put(self, request, id, *args, **kwargs):

        try:
            post = Post.objects.get(pk=id)
            serializer = PostUpdateSerializer(data=request.data, instance=post)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'post': serializer.data
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'status': False,
                    'message': 'update post fail',
                    'post': []
                })
        except Exception as e:
            return Response({
                'status': False,
                'message': str(e),
                'post': []
            })
