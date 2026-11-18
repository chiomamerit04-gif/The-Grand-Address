
from django.db import migrations


def add_missing_booking_columns(apps, schema_editor):
    Booking = apps.get_model('bookings', 'Booking')

    with schema_editor.connection.cursor() as cursor:
        existing_columns = {
            column.name
            for column in schema_editor.connection.introspection.get_table_description(
                cursor, Booking._meta.db_table
            )
        }

    for field_name in ['full_name', 'email', 'date_created']:
        field = Booking._meta.get_field(field_name)

        if field.column not in existing_columns:
            schema_editor.add_field(Booking, field)
            existing_columns.add(field.column)


def remove_booking_columns(apps, schema_editor):
    Booking = apps.get_model('bookings', 'Booking')

    for field_name in ['date_created', 'email', 'full_name']:
        field = Booking._meta.get_field(field_name)

        with schema_editor.connection.cursor() as cursor:
            existing_columns = {
                column.name
                for column in schema_editor.connection.introspection.get_table_description(
                    cursor, Booking._meta.db_table
                )
            }

        if field.column in existing_columns:
            schema_editor.remove_field(Booking, field)


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_booking_check_in_booking_check_out'),
    ]

    operations = [
        migrations.RunPython(
            add_missing_booking_columns,
            remove_booking_columns,
        ),
    ]
