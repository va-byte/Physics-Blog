# Generated by Django 3.0.3 on 2020-10-25 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
