# Generated by Django 4.2.11 on 2024-03-13 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='id',
            new_name='img_id',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]