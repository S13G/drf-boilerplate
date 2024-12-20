import uuid

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """
    An abstract base class model that provides self-updating
    `created_at` and `updated_at` fields, as well as `created_by`,
    `updated_by`, and `is_active` for status tracking.
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, db_index=True
    )
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True  # This model will not create a database table by itself
        ordering = ["-created_at"]  # Default ordering based on creation time
        verbose_name = "Base Model"
        verbose_name_plural = "Base Models"

    def __str__(self):
        return f"{self.__class__.__name__} (created at {self.created_at})"


class BlacklistedToken(models.Model):
    jti = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Blacklisted Token"
        verbose_name_plural = "Blacklisted Tokens"

    def __str__(self):
        return f"Blacklisted token with jti: {self.jti}"
