# Generated by Django 3.0.5 on 2020-04-06 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qnaapi', '0003_auto_20200406_0605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='avatar',
            new_name='icon',
        ),
    ]
