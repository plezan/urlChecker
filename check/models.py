from django.db import models
import re

# Create your models here.
class Check(models.Model):

    class CheckTypes(models.IntegerChoices):
        HTTP_CODE = 1
        HTTP_BODY = 2

    check_type = models.PositiveSmallIntegerField(
        verbose_name='Check type',
        choices=CheckTypes.choices,
        default=CheckTypes.HTTP_CODE,
        null=False,
        blank=False
    )
    succes_value = models.TextField(
        max_length=256,
        verbose_name='Value awaited for success',
        null=False,
        blank=False
    )

    description = models.TextField(
        max_length=256,
        verbose_name='Check description',
        null=True,
        blank=True,
        default=None
    )

    url = models.ForeignKey(
        "addresses.Address",
        on_delete=models.SET_NULL,
        verbose_name = "Url to check",
        db_index=True,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return str(self.check_type)

    class Meta:
        verbose_name = "Check"
        verbose_name_plural = "Checks"
