# Generated by Django 4.0.4 on 2022-09-26 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_api", "0005_user_user cant followed by self"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="user",
            name="User cant followed by self",
        ),
    ]