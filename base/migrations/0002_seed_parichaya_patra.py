from django.db import migrations


def create_field(FormField, subcategory, order, label, name, placeholder="", section=""):
    FormField.objects.get_or_create(
        subcategory=subcategory,
        name=name,
        defaults={
            "label": label,
            "placeholder": placeholder or label,
            "section": section,
            "order": order,
        },
    )


def seed_parichaya_patra(apps, schema_editor):
    MainCategory = apps.get_model("base", "MainCategory")
    SubCategory = apps.get_model("base", "SubCategory")
    FormField = apps.get_model("base", "FormField")

    category, _ = MainCategory.objects.get_or_create(
        slug="parichaya-patra",
        defaults={"name": "परिचय पत्र", "order": 1},
    )

    subcategories = {
        "mahila": ("महिला", "woman", 1),
        "balbalika": ("बालबालिका", "children", 2),
        "apanga": ("अपाङ्गता", "wheelchair", 3),
        "apanga-bhatta": ("अपाङ्ग भत्ता", "id-card", 4),
    }

    created_subcategories = {}
    for slug, (name, icon, order) in subcategories.items():
        subcategory, _ = SubCategory.objects.get_or_create(
            main_category=category,
            slug=slug,
            defaults={"name": name, "icon": icon, "order": order},
        )
        created_subcategories[slug] = subcategory

    common_fields = [
        ("पहिलो नाम", "first-name", "पहिलो नाम", "व्यक्तिगत विवरण"),
        ("बिचको नाम", "middle-name", "बिचको नाम", "व्यक्तिगत विवरण"),
        ("थर", "last-name", "थर", "व्यक्तिगत विवरण"),
        ("प्रदेश", "province", "प्रदेश", "स्थायी ठेगाना"),
        ("जिल्ला", "district", "जिल्ला", "स्थायी ठेगाना"),
        ("गा.बी.स / न.पा", "local-level", "स्थायी ठेगाना", "स्थायी ठेगाना"),
        ("वडा नं.", "ward-number", "वडा नं", "स्थायी ठेगाना"),
        ("टोल", "tole", "टोल", "स्थायी ठेगाना"),
    ]

    mahila_fields = common_fields + [
        ("बुवाको पहिलो नाम", "father-first-name", "बुवाको पहिलो नाम", "बुवाको विवरण"),
        ("बुवाको बिचको नाम", "father-middle-name", "बुवाको बिचको नाम", "बुवाको विवरण"),
        ("बुवाको थर", "father-last-name", "बुवाको थर", "बुवाको विवरण"),
        ("आमाको पहिलो नाम", "mother-first-name", "आमाको पहिलो नाम", "आमाको विवरण"),
        ("आमाको बिचको नाम", "mother-middle-name", "आमाको बिचको नाम", "आमाको विवरण"),
        ("आमाको थर", "mother-last-name", "आमाको थर", "आमाको विवरण"),
        ("बाजेको पहिलो नाम", "grandfather-first-name", "बाजेको पहिलो नाम", "बाजेको विवरण"),
    ]

    balbalika_fields = common_fields + [
        ("अभिभावकको नाम", "guardian-name", "अभिभावकको नाम", "अभिभावक विवरण"),
        ("जन्म मिति", "date-of-birth", "जन्म मिति", "बालबालिका विवरण"),
        ("जन्म दर्ता नं.", "birth-registration-number", "जन्म दर्ता नं.", "बालबालिका विवरण"),
    ]

    for index, field in enumerate(mahila_fields, start=1):
        create_field(FormField, created_subcategories["mahila"], index, *field)

    for index, field in enumerate(balbalika_fields, start=1):
        create_field(FormField, created_subcategories["balbalika"], index, *field)


def unseed_parichaya_patra(apps, schema_editor):
    MainCategory = apps.get_model("base", "MainCategory")
    MainCategory.objects.filter(slug="parichaya-patra").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_parichaya_patra, unseed_parichaya_patra),
    ]
