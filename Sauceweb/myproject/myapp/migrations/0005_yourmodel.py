# Generated by Django 5.1.6 on 2025-05-13 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_diary_delete_dailyreport"),
    ]

    operations = [
        migrations.CreateModel(
            name="YourModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("description", models.TextField(max_length=300)),
            ],
        ),
    ]
