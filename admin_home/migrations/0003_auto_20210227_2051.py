# Generated by Django 3.1.5 on 2021-02-27 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_home', '0002_auto_20210227_2025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_details',
            old_name='img_url',
            new_name='images',
        ),
    ]