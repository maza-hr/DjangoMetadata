# Generated by Django 4.2.7 on 2023-11-24 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app_satoc", "0004_feedback"),
    ]

    operations = [
        migrations.CreateModel(
            name="company",
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
                ("company", models.CharField(max_length=100, verbose_name="Company")),
            ],
        ),
        migrations.RemoveField(
            model_name="feedback",
            name="comentario",
        ),
        migrations.RemoveField(
            model_name="feedback",
            name="funcao",
        ),
        migrations.RemoveField(
            model_name="feedback",
            name="nome_completo",
        ),
        migrations.AddField(
            model_name="feedback",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="feedback",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="First name"
            ),
        ),
        migrations.AddField(
            model_name="feedback",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Last name"
            ),
        ),
        migrations.AddField(
            model_name="feedback",
            name="role_job_title",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Role or Job Title"
            ),
        ),
        migrations.AddField(
            model_name="feedback",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app_satoc.company",
                verbose_name="Final Database",
            ),
        ),
    ]
