# Generated by Django 3.2.9 on 2021-11-08 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'managed': True, 'verbose_name': 'Компания', 'verbose_name_plural': 'Каомпании'},
        ),
        migrations.AlterModelTable(
            name='company',
            table='',
        ),
    ]