from django.db import migrations


def create_user_table_if_missing(apps, schema_editor):
    User = apps.get_model("base", "User")
    existing_tables = schema_editor.connection.introspection.table_names()

    if User._meta.db_table not in existing_tables:
        schema_editor.create_model(User)


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0014_user"),
    ]

    operations = [
        migrations.RunPython(create_user_table_if_missing, migrations.RunPython.noop),
    ]
