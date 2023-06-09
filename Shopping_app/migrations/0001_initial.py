# Generated by Django 4.1.2 on 2023-05-05 04:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Volcano',
            fields=[
                ('Volcano_ID', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Volcano_Name', models.CharField(max_length=100)),
                ('Volcano_Image', models.URLField(max_length=100)),
                ('Volcano_Type', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('epoch_period', models.CharField(max_length=100)),
                ('Latitude', models.CharField(max_length=50)),
                ('Longitude', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='Shopping_app.cart')),
                ('volcano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shopping_app.volcano')),
            ],
        ),
    ]
