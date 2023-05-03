from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group, Permission, AbstractUser, BaseUserManager
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import UserManager


class CustomUserManager(BaseUserManager):
    pass  # 保留为空，您可以根据需要添加自定义方法

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='custom_users'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='custom_users'
    )

    objects = UserManager()  # 更新这一行，使用导入的 UserManager

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not hasattr(self, 'customer'):
            Customer.objects.create(user=self)

    def clean(self):
        super(AbstractUser, self).clean()  # 调用 AbstractBaseUser 的 clean 方法而不是 AbstractUser
        self.email = self.__class__.objects.normalize_email(self.email)


class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, related_name='customer', blank=True, null=True)

