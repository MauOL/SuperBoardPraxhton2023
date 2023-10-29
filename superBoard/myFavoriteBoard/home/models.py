from django.db import models
import django.utils.timezone

# Create your models here.
class Consultor(models.Model):
   clave  = models.CharField(max_length=4)
   nombre = models.CharField(max_length=100)
   area   = models.CharField(max_length=35)

class AvatarConfig(models.Model):
   id_consultor = models.IntegerField()
   cualidades   = models.CharField(max_length=180)
   nombre_foto  = models.CharField(max_length=100)
   color_fondo  = models.CharField(max_length=30)

# Valores del campo estatus:
# 1: Asignada, 2: En Progreso, 3: Concluida
class Actividad(models.Model):
   id_consultor = models.IntegerField()
   descrip      = models.CharField(max_length=120)
   categoria    = models.CharField(max_length=100)
   proyecto     = models.CharField(max_length=100)
   valor        = models.IntegerField()
   estatus      = models.IntegerField()
   notas        = models.CharField(max_length=150)
   fecha_asignacion = models.DateField()
   fecha_entrega    = models.DateField()

class Bonus(models.Model):
   id_consultor = models.IntegerField()
   descrip      = models.CharField(max_length=70)
   valor        = models.IntegerField()
   fecha_asignacion = models.DateField()

class CalculoTotales(models.Model):
   id_consultor      = models.IntegerField()
   total_valor_acts  = models.IntegerField(default=0)
   total_valor_bonus = models.IntegerField(default=0)
   total_valor       = models.IntegerField(default=0)
   fecha_calculo     = models.DateField(default=django.utils.timezone.now)