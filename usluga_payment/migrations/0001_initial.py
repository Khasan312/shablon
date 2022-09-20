# Generated by Django 4.0.6 on 2022-09-09 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Podiezd",
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
                ("token", models.CharField(max_length=100)),
                ("account_number", models.IntegerField(max_length=50)),
                ("refill_date_time", models.DateTimeField(auto_now_add=True)),
                ("amount", models.IntegerField(max_length=10)),
                ("action", models.CharField(max_length=50)),
            ],
        ),
    ]
