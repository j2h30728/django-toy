# Generated by Django 5.1.1 on 2024-09-30 16:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tweets", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="like",
            name="tweet",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="likes",
                to="tweets.tweet",
            ),
        ),
    ]
