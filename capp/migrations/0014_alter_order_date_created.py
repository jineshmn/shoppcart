# Generated by Django 3.2 on 2021-06-01 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capp', '0013_auto_20210601_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
