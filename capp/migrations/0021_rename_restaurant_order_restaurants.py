# Generated by Django 3.2 on 2021-06-03 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capp', '0020_auto_20210603_1937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='restaurant',
            new_name='restaurants',
        ),
    ]