from django.db import migrations


def fix_rayak_no_category_label(apps, schema_editor):
    MainCategory = apps.get_model("base", "MainCategory")
    SubCategory = apps.get_model("base", "SubCategory")

    digital_file, _ = MainCategory.objects.get_or_create(name="Digital File Pranali")

    for old_name in ("रायको नं",):
        SubCategory.objects.filter(
            main_category=digital_file,
            name=old_name,
        ).delete()

    SubCategory.objects.get_or_create(
        main_category=digital_file,
        name="रायक नं",
    )


def unfix_rayak_no_category_label(apps, schema_editor):
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
        ("base", "0010_seed_rayako_no_category"),
    ]

    operations = [
        migrations.RunPython(fix_rayak_no_category_label, unfix_rayak_no_category_label),
    ]
