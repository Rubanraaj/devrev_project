# Generated by Django 4.2.2 on 2023-06-25 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='seat_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='flight',
            name='total_seats',
            field=models.IntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='booking',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.flight'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
