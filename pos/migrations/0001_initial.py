# Generated by Django 4.1.2 on 2022-12-05 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('example_app', '0004_bakedgood_baked_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructions', models.TextField()),
                ('baked_goods', models.ManyToManyField(to='example_app.bakedgood')),
            ],
        ),
    ]
