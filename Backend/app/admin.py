from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

admin.site.register(UserProfile)
admin.site.register(Child)
admin.site.register(Team)
admin.site.register(Achievement)
admin.site.register(Technique)
admin.site.register(Subscription)
admin.site.register(UserTechniqueRating)
