# Generated by Django 3.2.3 on 2021-05-22 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210521_2144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='body',
        ),
    ]
