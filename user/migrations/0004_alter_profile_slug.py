# Generated by Django 4.2.6 on 2023-11-20 17:54

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='name', unique=True),
        ),
    ]