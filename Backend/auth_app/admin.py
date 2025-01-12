from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from auth_app.models import User
from django.utils.translation import gettext_lazy as _

# Register your models here.





# in case that you want to sign in using email you can use the below code


# class CustomUserAdmin(UserAdmin):
#     fieldsets = (
#         (None, {"fields": ("email", "password")}),
#         (_("Personal info"), {"fields": ("first_name",
#                                          "last_name")}),
#         (
#             _("Permissions"),
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 )
#             },
#         ),
#         (_("Important dates"), {"fields": ("last_login",
#                                            )}),
#     )
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": ("email", "password1", "password2"),
#             },
#         ),
#     )
#     list_display = ("email", "first_name", "last_name",
#                     "is_staff")
#     search_fields = ("email", "first_name", "last_name")
#     ordering = ("email",)


# admin.site.register(User, CustomUserAdmin)
