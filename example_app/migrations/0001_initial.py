# Generated by Django 4.0.4 on 2022-06-16 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BakedGood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('desc', models.CharField(max_length=256)),
                ('good_type', models.CharField(choices=[('BG', 'Bagel'), ('BR', 'Bread'), ('CO', 'Cookie'), ('CA', 'Cake'), ('PR', 'Pretzel')], max_length=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('recipe', models.TextField()),
            ],
        ),
    ]
