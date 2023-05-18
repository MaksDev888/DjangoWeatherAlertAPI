from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserApp(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    bio = models.CharField(choices=GENDER, max_length=10, verbose_name="Gender")
    email = models.EmailField(_("email address"), unique=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date_joined"]
        verbose_name = "User"
        verbose_name_plural = "Users"
