# Generated by Django 4.1.5 on 2023-01-15 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web_profession", "0009_alter_cityfract_fraction"),
    ]

    operations = [
        migrations.CreateModel(
            name="CityLevel",
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
                ("city", models.CharField(max_length=20)),
                ("fraction", models.FloatField()),
            ],
        ),
    ]