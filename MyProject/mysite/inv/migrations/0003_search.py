# Generated by Django 3.0.3 on 2020-02-16 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0002_auto_20200214_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Searches',
            },
        ),
    ]
