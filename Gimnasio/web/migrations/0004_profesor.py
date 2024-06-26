# Generated by Django 5.0.6 on 2024-06-11 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_inscripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre')),
                ('dni', models.CharField(max_length=8, verbose_name='Dni')),
                ('email', models.EmailField(max_length=30, verbose_name='Email')),
                ('telefono', models.CharField(max_length=15, verbose_name='Plan')),
            ],
        ),
    ]