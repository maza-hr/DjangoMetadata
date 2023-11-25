# Generated by Django 4.2.7 on 2023-11-24 20:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_satoc", "0003_alter_originalfilename_ofn_ofs"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
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
                ("nome_completo", models.CharField(max_length=100)),
                ("funcao", models.CharField(max_length=50)),
                ("comentario", models.TextField()),
            ],
        ),
    ]
