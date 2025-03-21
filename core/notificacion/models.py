from django.db import models
from ..delegacion.models import Delegacion
from datetime import datetime


class Notificacion(models.Model):
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    motivo=models.CharField(verbose_name='Motivo',db_column='MOTIVO',max_length=50,null=False,blank=False)
    mensaje=models.CharField(verbose_name='Mensaje',db_column='MENSAJE',max_length=350,null=False,blank=True)
    emisor=models.ForeignKey(Delegacion,verbose_name='Emisor',db_column='EMISOR',on_delete=models.CASCADE)
    leido=models.BooleanField(verbose_name='Leído',db_column='LEIDO',default=False)
    fechahora=models.DateTimeField(verbose_name='Feha y Hora',db_column='FECHA_HORA',blank=False,null=False,default=datetime.now,editable=False)

    class Meta:
        db_table='NOTIFICACION'
        verbose_name='NOTIFICACION'
        verbose_name_plural='NOTIFICACIONES'


    def __str__(self):
        return f'{self.mensaje} \u1F5F8' if self.leido else f'{self.mensaje}'

class Destinatario(models.Model):
    id=models.BigAutoField(verbose_name='ID',db_column='ID',primary_key=True)
    usuario=models.ForeignKey(Delegacion,verbose_name='Destinatario',db_column='USUARIO',on_delete=models.SET_NULL,null=True)
    notificacion=models.ForeignKey(Notificacion,verbose_name='Notificación',db_column='NOTIFICACION_ID',on_delete=models.CASCADE)

    class Meta:
        db_table='DESTINATARIO'
        verbose_name='DESTINATARIO'
        verbose_name_plural='DESTINATARIOS'

    
    def __str__(self):
        return f'{self.usuario.delegacion}' if f'{self.usuario.delegacion}' else f'{self.usuario.username}'