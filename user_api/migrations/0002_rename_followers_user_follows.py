# Generated by Django 4.0.4 on 2022-09-27 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='followers',
            new_name='follows',
        ),
    ]
