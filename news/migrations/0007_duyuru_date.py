# Generated by Django 4.1.4 on 2025-04-21 03:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0006_remove_haber_resim2_remove_haber_resim3_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="duyuru",
            name="date",
            field=models.DateField(
                blank=True, default=django.utils.timezone.now, null=True
            ),
        ),
    ]
