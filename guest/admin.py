from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import Guest, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def has_permission(self, request):
        """
        Removed check for is_staff.
        """
        return request.user.is_active

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    pass