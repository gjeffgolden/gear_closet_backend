# Generated by Django 3.1.7 on 2021-03-24 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0003_auto_20210319_1428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='image',
            new_name='image_url',
        ),
        migrations.RemoveField(
            model_name='item',
            name='purchased_year',
        ),
    ]