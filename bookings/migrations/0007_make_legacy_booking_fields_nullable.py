
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_fix_missing_booking_columns'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                ALTER TABLE bookings_booking
                ALTER COLUMN guests DROP NOT NULL;

                ALTER TABLE bookings_booking
                ALTER COLUMN total_price DROP NOT NULL;

                ALTER TABLE bookings_booking
                ALTER COLUMN user_id DROP NOT NULL;
            """,
            reverse_sql="""
                ALTER TABLE bookings_booking
                ALTER COLUMN guests SET NOT NULL;

                ALTER TABLE bookings_booking
                ALTER COLUMN total_price SET NOT NULL;

                ALTER TABLE bookings_booking
                ALTER COLUMN user_id SET NOT NULL;
            """
        ),
    ]

