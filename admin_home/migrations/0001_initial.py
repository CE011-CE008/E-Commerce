# Generated by Django 3.1.5 on 2021-02-21 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=10000)),
                ('product_date', models.DateField()),
            ],
            options={
                'db_table': 'product_details',
            },
        ),
    ]
