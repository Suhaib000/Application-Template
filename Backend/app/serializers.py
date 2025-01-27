from rest_framework import serializers
from .models import *
from drf_writable_nested import WritableNestedModelSerializer
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name' , 'last_name','email','is_staff','is_active','username','groups']



class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = "__all__"

class TechniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technique
        fields = "__all__"

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class UserTechniqueRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTechniqueRating
        fields = "__all__"



class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        # fields = "__all__"
        fields = ['name', 'age']



# class UserProfileSerializer(serializers.ModelSerializer):
class UserProfileSerializer(WritableNestedModelSerializer):
    user  = UserSerializer(read_only=True)
    children = ChildSerializer(many=True,read_only=True)
    ratings = UserTechniqueRatingSerializer(many=True, read_only=True) 
    achievements = AchievementSerializer(many=True, read_only=True) 
    subscriptions = SubscriptionSerializer(read_only=True) 

    class Meta:
        model = UserProfile
        fields = "__all__"


