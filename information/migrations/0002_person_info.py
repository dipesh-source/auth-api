# Generated by Django 4.1.1 on 2022-10-12 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("information", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Person_info",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("age", models.IntegerField()),
                ("city", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
            ],
        ),
    ]
