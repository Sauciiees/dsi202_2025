# Generated by Django 5.1.6 on 2025-05-14 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0006_workout_delete_yourmodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workout",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
