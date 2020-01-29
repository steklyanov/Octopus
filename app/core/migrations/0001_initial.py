# Generated by Django 3.0.2 on 2020-01-28 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sex', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('bust', models.IntegerField(blank=True, null=True)),
                ('waist', models.IntegerField(blank=True, null=True)),
                ('hips', models.IntegerField(blank=True, null=True)),
                ('shoe', models.IntegerField(blank=True, null=True)),
                ('hair', models.CharField(blank=True, choices=[('BROWN', 'Brown'), ('BLACK', 'Black'), ('AUBUR', 'Auburn'), ('RED', 'Red'), ('WHITE', 'Grey or white')], max_length=5)),
                ('eyes', models.CharField(blank=True, choices=[('AMB', 'Amber'), ('BLU', 'Blue'), ('BRO', 'Brown'), ('GRA', 'Gray'), ('GRE', 'Green'), ('HAZ', 'Hazel')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Booker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default=None, max_length=255, null=True, unique=True)),
                ('agency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Agency')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, default=None, max_digits=6)),
                ('client', models.ManyToManyField(to='core.Client')),
                ('models_id', models.ManyToManyField(to='core.Actor')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobs', models.ManyToManyField(blank=True, to='core.Job')),
            ],
        ),
        migrations.CreateModel(
            name='NestedField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Agency')),
                ('booker', models.ManyToManyField(to='core.Booker')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='schedule',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Schedule'),
        ),
        migrations.AddField(
            model_name='booker',
            name='schedule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Schedule'),
        ),
        migrations.AddField(
            model_name='booker',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='actor',
            name='agency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Agency'),
        ),
        migrations.AddField(
            model_name='actor',
            name='schedule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Schedule'),
        ),
    ]
