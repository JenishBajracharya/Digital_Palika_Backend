from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0011_fix_rayak_no_category_label"),
    ]

    operations = [
        migrations.CreateModel(
            name="RayakNo",
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
                ("rayak_no", models.CharField(max_length=100, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "main_category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="rayak_nos",
                        to="base.maincategory",
                    ),
                ),
                (
                    "sub_category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="rayak_nos",
                        to="base.subcategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Rayak No",
                "verbose_name_plural": "Rayak Nos",
                "ordering": ["-created_at"],
            },
        ),
    ]
