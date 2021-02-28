# Generated by Django 3.1.5 on 2021-02-25 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_home', '0011_auto_20210224_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200)),
                ('product_name', models.CharField(max_length=200)),
                ('total', models.IntegerField()),
                ('amount', models.FloatField()),
            ],
        ),
    ]