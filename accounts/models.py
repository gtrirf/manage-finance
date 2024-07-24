from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.utils import timezone
import random



class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    fullname = models.CharField(blank=True, null=True, max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text=_('The groups this user belongs to.'),
        verbose_name=_('groups')
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',
        blank=True,
        help_text=_('Specific permissions for this user.'),
        verbose_name=_('user permissions')
    )

    def __str__(self):
        return self.email


class VerificationCode(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, db_index=True)
    created_at = models.DateTimeField(default=timezone.now)

    def is_valid(self):
        return (timezone.now() - self.created_at).total_seconds() < 3600

    def generate_code(self):
        self.code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        print(self.code)
        self.save()

    def __str__(self):
        return f"{self.user.email} - {self.code}"
