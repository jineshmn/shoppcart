# Generated by Django 3.2.2 on 2021-06-21 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capp', '0027_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]