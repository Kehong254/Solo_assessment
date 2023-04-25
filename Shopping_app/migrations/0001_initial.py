# Generated by Django 4.2 on 2023-04-25 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volcano',
            fields=[
                ('Volcano_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Volcano_Name', models.TextField(max_length=100)),
                ('Volcano_Image', models.URLField(max_length=100)),
                ('Volcano_Type', models.TextField(max_length=100)),
                ('Country', models.TextField(max_length=100)),
                ('epoch_period', models.TextField(max_length=100)),
                ('Latitude', models.TextField()),
                ('Longitude', models.TextField()),
            ],
        ),
    ]