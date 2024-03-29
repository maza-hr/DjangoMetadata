# Generated by Django 4.2.7 on 2023-11-20 02:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_satoc", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="domainepsg",
            name="dom_nm_epsg",
            field=models.CharField(max_length=30, verbose_name="EPSG Name"),
        ),
        migrations.AlterField(
            model_name="domainepsg",
            name="dom_sg_epsg",
            field=models.CharField(max_length=20, verbose_name="EPSG Acronym"),
        ),
    ]
