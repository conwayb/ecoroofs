import uuid

from django.db import migrations, models
from django.contrib.auth import get_user_model

import arcutils.decorators

import ecoroofs.models


def make_initial_pages(apps, schema_editor):
    user_model = get_user_model()
    user, _ = user_model.objects.get_or_create(username='__migrations__', is_active=False)
    model = apps.get_model('pages', 'Page')
    data = [
        {'title': 'About'},
        {'title': 'Contact'},
    ]
    args = []
    for order, d in enumerate(data):
        title = d['title']
        page_args = {
            'description': title,
            'content': title,
            'published': True,
        }
        page_args.update(d)
        args.append(page_args)
    model.objects.bulk_create(model(**a) for a in args)


class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', ecoroofs.models.UUIDPrimaryKeyField(default=uuid.uuid4, serialize=False)),
                ('slug', ecoroofs.models.UniqueDerivedSlugField(blank=True, editable=False, max_length=255, source_field='title')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('content', models.TextField()),
                ('published', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model, arcutils.decorators.CachedPropertyInvalidatorMixin),
        ),

        migrations.RunPython(make_initial_pages)
    ]
