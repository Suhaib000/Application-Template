from django.db import models

from django.contrib.auth.models import User


# Profile model extending the User model


class Team(models.Model):
    team_name = models.CharField(max_length=255)
    coach_name = models.CharField(max_length=255)
    leader_name = models.CharField(max_length=255)
    def __str__(self):
        return self.team_name
    
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('admin_assist', 'Admin Assistant'),
        ('coach', 'Coach'),
        ('trainee', 'Trainee'),
    ]
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='trainee')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    age = models.IntegerField()
    occupation = models.CharField(max_length=255)
    height = models.FloatField()
    weight = models.FloatField()
    training_level = models.CharField(max_length=255)
    team_join_date = models.DateField()    
    speed_level = models.CharField(max_length=1, choices=[('S', 'Slow'), ('M', 'Medium'), ('G', 'Good')])
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_info",null=True)

    def __str__(self):
        return self.user.username

class Child(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="children")
    name = models.CharField(max_length=255)
    age = models.IntegerField()


class Achievement(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="achievements")
    badge_name = models.CharField(max_length=255)

class Subscription(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="subscriptions")
    subscription_img = models.ImageField(upload_to='backend/media/subscription_images/')
    subscription_status= models.BooleanField(default=False)
    subscription_end_date = models.DateField()


class Technique(models.Model):
    name = models.CharField(max_length=255)  # Name of the technique

    def __str__(self):
        return self.name

class UserTechniqueRating(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="ratings")
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE, related_name="ratings")
    rating = models.IntegerField()  # Rating for the technique (e.g., 1-10 scale)

    class Meta:
        unique_together = ('user_profile', 'technique')  # Ensure one rating per user per technique

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.technique.name} - {self.rating}"