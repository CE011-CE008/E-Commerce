# Generated by Django 3.1.5 on 2021-02-24 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_home', '0005_auto_20210224_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receivedproduct',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
