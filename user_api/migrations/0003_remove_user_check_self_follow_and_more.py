# Generated by Django 4.0.4 on 2022-09-26 10:56

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ("user_api", "0002_alter_user_user_from_alter_user_user_to"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="user",
            name="check_self_follow",
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("user_from", django.db.models.expressions.F("user_to")),
                    _negated=True,
                ),
                name="User cant follow to self",
            ),
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("user_to", django.db.models.expressions.F("user_from"))
                ),
                name="User cant followed by self",
            ),
        ),
    ]
