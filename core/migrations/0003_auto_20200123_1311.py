# Generated by Django 3.0.2 on 2020-01-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200121_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booker',
            name='email',
            field=models.EmailField(default=None, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=6),
        ),
    ]
