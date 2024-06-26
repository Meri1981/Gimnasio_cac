# Generated by Django 5.0.6 on 2024-06-10 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_socio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inscripcion', models.DateTimeField(auto_now_add=True)),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.clase')),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.socio')),
            ],
        ),
    ]
