import posixpath

from django.db import models
from django.core.urlresolvers import reverse

from arcutils.decorators import cached_property, CachedPropertyInvalidatorMixin

from ..models import BaseModel, UniqueDerivedSlugField


class Page(BaseModel, CachedPropertyInvalidatorMixin):

    class Meta:
        ordering = ['title']

    title = models.CharField(max_length=255)
    slug = UniqueDerivedSlugField(source_field='title')
    description = models.TextField(null=True, blank=True)
    content = models.TextField()
    published = models.BooleanField(default=False)

    @cached_property('slug')
    def url(self):
        return posixpath.join(reverse('page', kwargs={'slug': self.slug}))

    def __str__(self):
        return '{self.title} at {self.url}'.format(self=self)
