from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
from users.models import ProfileUser


class ProfileUserInline(admin.StackedInline):
    model = ProfileUser
    can_delete = False
    verbose_name_plural = 'profileuser'


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ProfileUserInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
