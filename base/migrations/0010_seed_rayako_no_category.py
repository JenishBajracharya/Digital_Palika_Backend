from django.db import migrations


def seed_rayako_no_category(apps, schema_editor):
    MainCategory = apps.get_model("base", "MainCategory")
    SubCategory = apps.get_model("base", "SubCategory")

    digital_file, _ = MainCategory.objects.get_or_create(name="Digital File Pranali")
    SubCategory.objects.get_or_create(
        main_category=digital_file,
        name="रायक नं",
    )


def unseed_rayako_no_category(apps, schema_editor):
    MainCategory = apps.get_model("base", "MainCategory")
    SubCategory = apps.get_model("base", "SubCategory")

    digital_file = MainCategory.objects.filter(name="Digital File Pranali").first()
    if digital_file:
        SubCategory.objects.filter(
            main_category=digital_file,
            name="रायक नं",
        ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0009_seed_digital_file_categories"),
    ]

    operations = [
        migrations.RunPython(seed_rayako_no_category, unseed_rayako_no_category),
    ]
