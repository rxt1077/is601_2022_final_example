# Generated by Django 4.1.2 on 2022-11-15 00:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('example_app', '0003_alter_bakedgood_good_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='bakedgood',
            name='baked_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
