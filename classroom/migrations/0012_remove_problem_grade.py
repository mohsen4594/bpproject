# Generated by Django 3.1.7 on 2021-03-07 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0011_auto_20210307_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='grade',
        ),
    ]