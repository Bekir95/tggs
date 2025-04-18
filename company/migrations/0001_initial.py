# Generated by Django 4.1.4 on 2025-03-05 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Il",
            fields=[
                (
                    "Sehir_Ismi",
                    models.CharField(
                        blank=True, max_length=200, primary_key=True, serialize=False
                    ),
                ),
                ("Sehir_Plaka_Kodu", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Ilce",
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
                ("Ilce_Ismi", models.CharField(max_length=100)),
                (
                    "Ilce_Sehir",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company.il",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="InsanKaynaklari",
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
                ("Ad", models.CharField(blank=True, max_length=100, null=True)),
                ("Sifat", models.CharField(blank=True, max_length=200, null=True)),
                ("Resim", models.ImageField(upload_to="djangouploads/company")),
                (
                    "Yonetici_Durumu",
                    models.CharField(
                        blank=True,
                        choices=[("Baskan", "Baskan"), ("Diger", "Diger")],
                        default="Diger",
                        max_length=50,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="YonetimKurulu",
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
                ("Ad", models.CharField(blank=True, max_length=100, null=True)),
                ("Sifat", models.CharField(blank=True, max_length=200, null=True)),
                ("Resim", models.ImageField(upload_to="djangouploads/company")),
                (
                    "Yonetici_Durumu",
                    models.CharField(
                        blank=True,
                        choices=[("Baskan", "Baskan"), ("Diger", "Diger")],
                        default="Diger",
                        max_length=50,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ilce_Baskanligi",
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
                (
                    "Yonetici_Ismi",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "Yonetici_Sifati",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("Yonetici_Biyografisi", models.TextField(blank=True, null=True)),
                (
                    "Yonetici_Resmi",
                    models.ImageField(
                        upload_to="djangouploads/teskilat/ilce_baskanligi/"
                    ),
                ),
                (
                    "Yonetici_Durumu",
                    models.CharField(
                        blank=True,
                        choices=[("Baskan", "Baskan"), ("Diger", "Diger")],
                        default="Diger",
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "Yonetici_Il",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company.ilce",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Il_Baskanligi",
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
                (
                    "Yonetici_Ismi",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "Yonetici_Sifati",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("Yonetici_Biyografisi", models.TextField(blank=True, null=True)),
                (
                    "Yonetici_Resmi",
                    models.ImageField(upload_to="djangouploads/company/"),
                ),
                (
                    "Yonetici_Durumu",
                    models.CharField(
                        blank=True,
                        choices=[("Baskan", "Baskan"), ("Diger", "Diger")],
                        default="Diger",
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "Yonetici_Il",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company.il",
                    ),
                ),
            ],
        ),
    ]
