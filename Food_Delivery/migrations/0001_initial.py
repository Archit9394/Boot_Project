# Generated by Django 2.1.5 on 2020-06-15 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('contact_phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('confirmation_code', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('time_joined', models.DateTimeField()),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Food_Delivery.city')),
            ],
        ),
        migrations.CreateModel(
            name='restaurants',
            fields=[
                ('restaurant_id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=255)),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Food_Delivery.city')),
            ],
        ),
    ]
