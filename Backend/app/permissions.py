from rest_framework import permissions
from .models import *


class IsAdmin(permissions.BasePermission):
    """ Full access for Admin users. """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff

class IsAdminAssess(permissions.BasePermission):
    """ Permission to manage UserProfile, Subscription, and Child. """
    def has_permission(self, request, view):
        group_names = request.user.groups.values_list('name', flat=True)
        return request.user.is_authenticated and (group_names[0]=='admin_assist')

class IsCoach(permissions.BasePermission):
    """ Permission to view UserProfiles in the same team and only list Subscriptions. """
    def has_permission(self, request, view):
        # group_names = request.user.groups.values_list('name', flat=True)
        # return request.user.is_authenticated and (group_names[0]=='Coach')
    # =======================================================================
        group_names = request.user.groups.values_list('name', flat=True)
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        
        # Check if the user is authenticated and belongs to an allowed group
        if request.user and request.user.is_authenticated:
            if group_names[0]=='Coach':
                # Allow editing but not deletion
                return request.method in ['PUT', 'PATCH']
        
        return False  # Deny all other cases

    def has_object_permission(self, request, view, obj):
        """ Coach can view only users in their team """
        return hasattr(request.user, 'profile') and obj.team == request.user.profile.team

class IsTrainee(permissions.BasePermission):
    """ Trainee can only view their own UserProfile and edit UserTechniqueRating. """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='trainee').exists()

    def has_object_permission(self, request, view, obj):
        """ Ensure Trainee can only edit their own ratings. """
        print('test2')
        if isinstance(obj, UserProfile):
            if request.method in ["GET", "HEAD", "OPTIONS"]:
                return True
        if isinstance(obj, UserTechniqueRating):
            print('test3')
            return obj.user_profile.user == request.user and request.method in ['PUT', 'PATCH']
        return False
