# Generated by Django 4.1.2 on 2022-10-18 19:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacion',
            name='fechahora',
            field=models.DateTimeField(db_column='FECHA_HORA', default=datetime.datetime.now, editable=False),
        ),
    ]
