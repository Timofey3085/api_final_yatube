from rest_framework import viewsets, mixins
from posts.models import Post, Group, Follow, Comment, User
from api.serializers import (CommentSerializer, GroupSerializer,
                             PostSerializer, FollowSerializer)
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsAuthorOrReadOnly
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет получения, записи и изменения постов."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Метод создания нового поста."""
        return serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет получения данных групп пользователей."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет получения, записи и изменения комментариев."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self):
        """Метод выбора всех комментариев по нужному посту."""
        return self.get_post().comments

    def perform_create(self, serializer):
        """Метод создания нового комментария по нужному посту."""
        serializer.save(author=self.request.user, post=self.get_post())


class FollowsViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """Вьюсет для обработки подписок."""
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ("following__username",)

    def get_queryset(self):

        following = get_object_or_404(User,
                                      username=self.request.user.username)
        return following.follower

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
