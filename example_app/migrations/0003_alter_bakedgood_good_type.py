# Generated by Django 4.1.2 on 2022-10-31 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_app', '0002_ingredient_bakedgood_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bakedgood',
            name='good_type',
            field=models.CharField(choices=[('BA', 'Bagel'), ('BR', 'Bread'), ('CO', 'Cookie'), ('CA', 'Cake'), ('PR', 'Pretzel')], max_length=2),
        ),
    ]