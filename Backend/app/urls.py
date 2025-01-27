from django.urls import path 

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
# from .views import UserViewSet

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet)
router.register(r'children', ChildViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'achievements', AchievementViewSet)
router.register(r'techniques', TechniqueViewSet)
router.register(r'subscription', SubscriptionViewSet)
router.register(r'UserTechniqueRating', UserTechniqueRatingViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
