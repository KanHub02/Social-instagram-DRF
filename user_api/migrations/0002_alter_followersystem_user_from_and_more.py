# Generated by Django 4.1.1 on 2022-09-30 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user_api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="followersystem",
            name="user_from",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="from_set",
                to=settings.AUTH_USER_MODEL,
                unique=True,
                verbose_name="By",
            ),
        ),
        migrations.AlterField(
            model_name="followersystem",
            name="user_to",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="to_set",
                to=settings.AUTH_USER_MODEL,
                unique=True,
                verbose_name="To",
            ),
        ),
    ]
