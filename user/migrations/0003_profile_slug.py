# Generated by Django 4.2.6 on 2023-11-13 18:39

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='name'),
        ),
    ]
