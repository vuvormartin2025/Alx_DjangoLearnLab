# accounts/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

def profile_picture_upload_to(instance, filename):
    return f'profile_pics/user_{instance.id}/{filename}'

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to=profile_picture_upload_to,
        blank=True,
        null=True
    )

    # Users this user follows (directional). Reverse name -> .followers
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )

    # Avoid reverse accessor clashes with the default auth models
    groups = models.ManyToManyField(
        Group,
        related_name='accounts_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='accounts_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def _str_(self):
        return self.username

    # convenience methods
    def follow(self, other_user):
        if other_user and other_user != self:
            self.following.add(other_user)

    def unfollow(self, other_user):
        if other_user and other_user != self:
            self.following.remove(other_user)

    def is_following(self, other_user):
        return self.following.filter(pk=other_user.pk).exists()