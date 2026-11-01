from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):
    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.RemoveField(model_name='booking', name='check_in'),
                migrations.RemoveField(model_name='booking', name='check_out'),
                migrations.RemoveField(model_name='booking', name='guests'),
                migrations.RemoveField(model_name='booking', name='total_price'),
                migrations.RemoveField(model_name='booking', name='user'),
                migrations.AddField(model_name='booking', name='date_created', field=models.DateTimeField(auto_now_add=True)),
                migrations.AddField(model_name='booking', name='email', field=models.EmailField(max_length=254)),
                migrations.AddField(model_name='booking', name='full_name', field=models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='booking',
            name='special_requests',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='property',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(),
        ),
    ]