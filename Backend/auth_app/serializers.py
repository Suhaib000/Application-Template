
# In case that you want to sign in using email you can use the below code

# from .models import User
# from rest_framework import serializers

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"
#         extra_kwargs = {
#             'password': {'write_only': True}  # Password is write-only
#         }


# # we use the below override to use setpassowrd for
#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         groups = validated_data.pop('groups', None)  # Extract M2M fields
#         user_permissions = validated_data.pop('user_permissions', None)
#         instance = self.Meta.model(**validated_data)
#         if password:
#             instance.set_password(password)
#         instance.save()

#         # Handle many-to-many fields
#         if groups:
#             instance.groups.set(groups)
#         if user_permissions:
#             instance.user_permissions.set(user_permissions)
        
#         return instance

#     def update(self, instance, validated_data):
#         password = validated_data.pop('password', None)
#         groups = validated_data.pop('groups', None)  # Extract M2M fields
#         user_permissions = validated_data.pop('user_permissions', None)
        
#         # Update fields
#         for attr, value in validated_data.items():
#             setattr(instance, attr, value)
#         if password:
#             instance.set_password(password)
#         instance.save()

#         # Handle many-to-many fields
#         if groups is not None:  # Explicit check for groups
#             instance.groups.set(groups)
#         if user_permissions is not None:  # Explicit check for user_permissions
#             instance.user_permissions.set(user_permissions)

#         return instance