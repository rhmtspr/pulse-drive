# Generated by Django 5.0.6 on 2024-05-21 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_car_price_alter_transaction_rental_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable'), ('under maintenance', 'Under maintenance')], default='Available', max_length=50),
        ),
    ]
