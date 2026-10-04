from django.db import models

# Create your models here.

from django.db import models
from django.utils.text import slugify


class BaseModel(models.Model):

    slug = models.SlugField(
        max_length=255,
        unique=True,
        editable=False,
        db_index=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True

    def get_slug_source(self):
        return ""

    def save(self, *args, **kwargs):

        if not self.slug:

            base_slug = slugify(
                self.get_slug_source()
            )

            slug = base_slug
            counter = 1

            while self.__class__.objects.filter(
                slug=slug
            ).exclude(
                pk=self.pk
            ).exists():

                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)