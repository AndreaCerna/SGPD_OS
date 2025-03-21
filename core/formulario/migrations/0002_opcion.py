# Generated by Django 4.1.2 on 2022-10-20 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='NOMBRE', max_length=250, verbose_name='Nombre')),
                ('pregunta', models.ForeignKey(db_column='PREGUNTA_ID', on_delete=django.db.models.deletion.CASCADE, to='formulario.pregunta', verbose_name='Pregunta')),
            ],
            options={
                'verbose_name': 'OPCION',
                'verbose_name_plural': 'OPCIONES',
                'db_table': 'OPCION',
            },
        ),
    ]
