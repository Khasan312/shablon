# Generated by Django 3.2.12 on 2022-09-10 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("usluga_payment", "0002_delete_podiezd"),
    ]

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
                ("account_number", models.IntegerField()),
                ("refill_date_time", models.DateTimeField(auto_now_add=True)),
                (
                    "amount",
                    models.DecimalField(decimal_places=3, max_digits=10),
                ),
                ("action", models.CharField(max_length=50)),
            ],
        ),
    ]
