# Generated by Django 4.1.2 on 2022-12-05 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
            preserve_default=False,
        ),
    ]
