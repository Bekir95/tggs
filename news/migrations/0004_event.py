# Generated by Django 4.1.4 on 2025-04-21 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0003_alter_duyuru_resim"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("title", models.CharField(max_length=200)),
                ("date", models.DateField()),
                ("description", models.TextField(blank=True)),
            ],
        ),
    ]
