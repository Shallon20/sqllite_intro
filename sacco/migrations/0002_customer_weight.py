# Generated by Django 5.1.3 on 2024-11-12 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sacco', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='weight',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
