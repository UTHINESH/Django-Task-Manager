# Generated by Django 4.2.11 on 2024-03-17 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Profile_pic',
            new_name='profile_pic',
        ),
    ]
