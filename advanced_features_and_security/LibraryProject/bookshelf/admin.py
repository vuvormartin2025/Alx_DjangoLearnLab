
from django.contrib import admin
from .models import Book

# Custom Admin configuration for the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns shown in the list view
    list_display = ("title", "author", "publication_year")

    # Sidebar filters
    list_filter = ("author", "publication_year")

    # Search functionality
    search_fields = ("title", "author")

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
