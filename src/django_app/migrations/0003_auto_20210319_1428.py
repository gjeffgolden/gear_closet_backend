# Generated by Django 3.1.7 on 2021-03-19 14:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0002_delete_kit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='year',
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='item',
            name='model_year',
            field=models.PositiveIntegerField(default=2021, validators=[django.core.validators.MaxValueValidator(2050), django.core.validators.MinValueValidator(1950)]),
        ),
        migrations.AddField(
            model_name='item',
            name='purchased_year',
            field=models.PositiveIntegerField(default=2021, validators=[django.core.validators.MaxValueValidator(2050), django.core.validators.MinValueValidator(1950)]),
        ),
        migrations.AddField(
            model_name='item',
            name='retired',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='item',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL),
        ),
    ]
