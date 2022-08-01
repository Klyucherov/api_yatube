from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from api.permissions import OnlyAuthorCanChangeContent
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Group, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [OnlyAuthorCanChangeContent, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [OnlyAuthorCanChangeContent, IsAuthenticated]

    def post_obj(self):
        queryset = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return queryset

    def get_queryset(self):
        return self.post_obj().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.post_obj())
