# Generated by Django 3.1.7 on 2021-03-24 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0004_auto_20210324_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image_url',
            field=models.CharField(max_length=500),
        ),
    ]