# Generated by Django 5.0.2 on 2024-07-25 07:23

import useraccount.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0002_alter_user_managers_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', useraccount.models.CustomUserManager()),
            ],
        ),
    ]