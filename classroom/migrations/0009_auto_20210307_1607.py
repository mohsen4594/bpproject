# Generated by Django 3.1.7 on 2021-03-07 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0008_auto_20210307_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='deadline',
            field=models.DateField(auto_now_add=True),
        ),
    ]
