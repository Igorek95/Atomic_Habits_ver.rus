from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(_("почта"), max_length=254, unique=True)
    is_active = models.BooleanField(_("активный аккаунт"), default=False)

    phone = models.CharField(_("телефон"), max_length=35, **NULLABLE)
    avatar = models.ImageField(_("аватар"), upload_to='users/', **NULLABLE)
    city = models.CharField(_("страна"), max_length=50)

    telegram_chat_id = models.CharField(_("чат ID в Telegram"), max_length=255, **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
