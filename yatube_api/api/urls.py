from rest_framework.routers import DefaultRouter
from django.urls import include, path
from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowsViewSet
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

v1_router = DefaultRouter()

v1_router.register(r'posts', PostViewSet)
v1_router.register(r'groups', GroupViewSet)
v1_router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comment')
v1_router.register(r'follow', FollowsViewSet)


jwt_patterns = [
    path('jwt/create/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(),
         name='token_verify'),
]

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include(jwt_patterns))
]
