# Generated by Django 4.1.2 on 2023-05-03 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping_app', '0007_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='Volcano_ID',
        ),
        migrations.AddField(
            model_name='cart',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]
