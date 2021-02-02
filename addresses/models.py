from django.db import models
import re

# Create your models here.
class Address(models.Model):

    url = models.TextField(
        max_length=256,
        verbose_name='URL',
        null=False,
        blank=False
    )

    name = models.TextField(
        max_length=128,
        verbose_name='Url name',
        null=True,
        blank=True,
        default=None
    )

    def __str__(self):
        if self.name :
            return self.name
        else :
            domainName = re.sub(r"https?://",'',self.url)
            domainName = re.match(r"^[^/\s]+",domainName).group()
            return domainName

    class Meta:
        verbose_name = "URL"
        verbose_name_plural = "URLs"
