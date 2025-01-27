from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from django.contrib.auth import get_user_model



@receiver(post_save, sender=UserProfile)
def assign_group_based_on_role(sender, instance, created, **kwargs):
    print("Test before create...")
    if created:  # Run only when a new user is created
        print("Test after create...")
        role_group_mapping = {
            'admin': 'Admins',
            'adminassess': 'AdminAssess',
            'coach': 'Coach',
            'trainee': 'Trainee',
        }
        print("instance.role = ",instance.role)
        
        group_name = role_group_mapping.get(instance.role)
        print("group_name = ",group_name)
        if group_name:
            group, _ = Group.objects.get_or_create(name=group_name)  # Create group if it doesn't exist
            instance.user.groups.add(group)  # Assign the user to the group




# to make user inactive in case we create new one to make admin activate the user ro login
User = get_user_model()

@receiver(post_save, sender=User)
def deactivate_new_user(sender, instance, created, **kwargs):
    if created and instance.is_active:  # If new user is created and active
        instance.is_active = False
        instance.save()