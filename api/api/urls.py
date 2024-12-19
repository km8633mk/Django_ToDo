from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, ProfileViewSet, EventViewSet, PhotoViewSet,
    PackingItemViewSet, MessageViewSet, FriendshipViewSet,
    FriendRequestViewSet, UserRegistrationView, UserLoginView, UserLogoutView
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'events', EventViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'packing-items', PackingItemViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'friendships', FriendshipViewSet)
router.register(r'friend-requests', FriendRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
]

