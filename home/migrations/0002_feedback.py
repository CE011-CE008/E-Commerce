# Generated by Django 3.1.5 on 2021-03-03 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=25)),
                ('comment', models.CharField(max_length=2000)),
                ('status', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
    ]
