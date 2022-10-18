# Generated by Django 4.1.2 on 2022-10-18 19:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('formulario', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('respuesta', models.CharField(blank=True, db_column='RESPUESTA', max_length=350)),
                ('respondido', models.DateTimeField(db_column='FECHA_RESPONDIDO', default=datetime.datetime.now, editable=False)),
                ('latitud', models.CharField(db_column='LATITUD', max_length=12)),
                ('longitud', models.CharField(db_column='LONGITUD', max_length=13)),
                ('delegacion', models.ForeignKey(db_column='DELEGACION_ID', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pregunta', models.ForeignKey(db_column='PREGUNTA_ID', on_delete=django.db.models.deletion.CASCADE, to='formulario.pregunta')),
            ],
            options={
                'verbose_name': 'RESPUESTA',
                'verbose_name_plural': 'RESPUESTAS',
                'db_table': 'RESPUESTA',
            },
        ),
    ]
