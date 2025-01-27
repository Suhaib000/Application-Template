from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from .permissions import *
from django.contrib.auth.models import Group
from rest_framework.permissions import DjangoModelPermissions


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [DjangoModelPermissions]
    # def get_permissions(self):
    #     group_info = self.request.user.groups.values('name').first()
    #     group_names = group_info['name'] if group_info else None
    #     # kindly handle the case where the user did not assign to group.

    #     if group_names == 'admin_assist':
    #          return [IsAuthenticated(), IsAdminAssess()]
    #     elif group_names == 'Coach':
    #          return [IsAuthenticated(), IsCoach()]
    #     return [IsAuthenticated(), IsTrainee()]


    # def get_queryset(self):
    #     """
    #     Restrict users to see only their own profile.
    #     """
    #     user = self.request.user
    #     group_names = user.groups.values_list('name', flat=True)

    #     if group_names[0] == "trainee":
    #         return UserProfile.objects.filter(user=user) 
    #     elif group_names[0] =="Coach": 
    #         print('user.profile.team Coach' , user.profile.team)
    #         return UserProfile.objects.filter(team=user.profile.team)
    #     return UserProfile.objects.all()

        
    

    def perform_create(self, serializer):
        try:
            # Save the UserProfile with the authenticated user
            user_profile = serializer.save(user=self.request.user)

            # Assign user to the corresponding group based on role
            role = user_profile.role  # Get role from the profile
            if user_profile.user:
                group, _ = Group.objects.get_or_create(name=role)  # Get or create the group
                user_profile.user.groups.add(group)  # Assign user to the group

        except IntegrityError:
            raise ValidationError({"error": "A profile for this user already exists."})
        

class ChildViewSet(ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class AchievementViewSet(ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class TechniqueViewSet(ModelViewSet):
    queryset = Technique.objects.all()
    serializer_class = TechniqueSerializer

class UserTechniqueRatingViewSet(ModelViewSet):
    queryset = UserTechniqueRating.objects.all()
    serializer_class = UserTechniqueRatingSerializer