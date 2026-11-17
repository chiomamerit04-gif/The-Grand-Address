
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_contactmessage'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunSQL(
                    sql='ALTER TABLE bookings_booking ALTER COLUMN check_in DROP NOT NULL;',
                    reverse_sql='ALTER TABLE bookings_booking ALTER COLUMN check_in SET NOT NULL;',
                ),
                migrations.RunSQL(
                    sql='ALTER TABLE bookings_booking ALTER COLUMN check_out DROP NOT NULL;',
                    reverse_sql='ALTER TABLE bookings_booking ALTER COLUMN check_out SET NOT NULL;',
                ),
            ],
            state_operations=[
                migrations.AddField(
                    model_name='booking',
                    name='check_in',
                    field=models.DateField(blank=True, null=True),
                ),
                migrations.AddField(
                    model_name='booking',
                    name='check_out',
                    field=models.DateField(blank=True, null=True),
                ),
            ],
        ),
    ]
