# Generated by Django 4.0.4 on 2022-07-14 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('desc', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='bakedgood',
            name='ingredients',
            field=models.ManyToManyField(to='example_app.ingredient'),
        ),
    ]
