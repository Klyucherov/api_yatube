from django.urls import include, path

from rest_framework import routers
from rest_framework.authtoken import views

from api.views import CommentViewSet, GroupReadOnlyViewSet, PostViewSet


v1_router = routers.DefaultRouter()

v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupReadOnlyViewSet)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
