# Generated by Django 4.0.4 on 2022-09-26 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_api", "0006_remove_user_user cant followed by self"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_private",
            field=models.BooleanField(default=False),
        ),
    ]
