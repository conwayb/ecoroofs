from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class SlugFieldMixin(models.Model):

    class Meta:
        abstract = True

    derive_slug_from = 'name'
    slug = models.SlugField(max_length=255, unique=True, blank=True)


@receiver(pre_save)
def set_slug(sender, instance, **kwargs):
    if issubclass(sender, SlugFieldMixin):
        field = instance.derive_slug_from
        value = getattr(instance, field)
        slug = slugify(value)
        instance.slug = slug
