# Generated by Django 3.0.7 on 2021-11-28 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20211128_0309'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
