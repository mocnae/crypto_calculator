# Generated by Django 4.1.3 on 2022-11-08 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='')),
                ('quote_usdt', models.FloatField()),
            ],
            options={
                'verbose_name': 'currency',
                'verbose_name_plural': 'currencys',
            },
        ),
    ]
