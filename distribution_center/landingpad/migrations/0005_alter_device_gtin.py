# Generated by Django 3.2.5 on 2021-07-06 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpad', '0004_auto_20210706_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='gtin',
            field=models.PositiveIntegerField(blank=True, max_length=100, verbose_name='gtin'),
        ),
    ]
