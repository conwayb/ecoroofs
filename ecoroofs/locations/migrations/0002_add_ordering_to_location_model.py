from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['name']},
        ),
    ]
