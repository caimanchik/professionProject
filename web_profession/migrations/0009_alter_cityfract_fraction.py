# Generated by Django 4.1.5 on 2023-01-15 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web_profession", "0008_skill"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cityfract", name="fraction", field=models.FloatField(),
        ),
    ]