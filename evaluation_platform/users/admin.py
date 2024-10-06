from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from evaluation_platform.users.models import (
    CustomUser,
    Department,
    Organization,
)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        "email",
        "first_name",
        "last_name",
        "department",
        "job_title",
        "is_staff",
        "is_active",
        "years_of_service",
    )
    list_filter = ("email", "is_staff", "is_active", "department", "role")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "department",
                    "job_title",
                    "date_hired",
                )
            },
        ),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "department",
                    "job_title",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = ("email", "first_name", "last_name", "department")
    ordering = ("email",)


class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = (
        "name",
        "abbreviation",
    )


class OrganizationAdmin(admin.ModelAdmin):
    model = Organization
    list_display = (
        "name",
        "abbreviation",
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Organization, OrganizationAdmin)
