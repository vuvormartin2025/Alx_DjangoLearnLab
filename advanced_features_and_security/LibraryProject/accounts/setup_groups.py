from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from advanced_features_and_security.models import Book

def setup_groups():
    content_type = ContentType.objects.get_for_model(Book)

    # Permissions
    can_view = Permission.objects.get(codename="can_view", content_type=content_type)
    can_create = Permission.objects.get(codename="can_create", content_type=content_type)
    can_edit = Permission.objects.get(codename="can_edit", content_type=content_type)
    can_delete = Permission.objects.get(codename="can_delete", content_type=content_type)

    # Create Groups
    viewers, _ = Group.objects.get_or_create(name="Viewers")
    editors, _ = Group.objects.get_or_create(name="Editors")
    admins, _ = Group.objects.get_or_create(name="Admins")

    # Assign Permissions
    viewers.permissions.set([can_view])
    editors.permissions.set([can_view, can_create, can_edit])
    admins.permissions.set([can_view, can_create, can_edit, can_delete])

    print("Groups and permissions set up successfully!")


from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from advanced_features_and_security.models import Book

class Command(BaseCommand):
    help = "Set up default groups and assign permissions"

    def handle(self, *args, **kwargs):
        # Fetch permissions
        can_view = Permission.objects.get(codename="can_view")
        can_create = Permission.objects.get(codename="can_create")
        can_edit = Permission.objects.get(codename="can_edit")
        can_delete = Permission.objects.get(codename="can_delete")

        # Create groups
        viewers, _ = Group.objects.get_or_create(name="Viewers")
        editors, _ = Group.objects.get_or_create(name="Editors")
        admins, _ = Group.objects.get_or_create(name="Admins")

        # Assign permissions
        viewers.permissions.set([can_view])
        editors.permissions.set([can_view, can_create, can_edit])
        admins.permissions.set([can_view, can_create, can_edit, can_delete])

        self.stdout.write(self.style.SUCCESS("Groups and permissions created successfully."))