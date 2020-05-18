from django.db import models
from datetime import datetime
# Create your models here.

class Empleado(models.Model):
    names= models.CharField(max_length=150, verbose_name='Nombres')
    ine=models.CharField(max_length=10, unique=True, verbose_name='INE')
    date_joined=models.DateTimeField(default=datetime.now, verbose_name='Fecha de registro')
    date_creation=models.DateTimeField(auto_now=True)
    date_updated=models.DateTimeField(auto_now_add=True)
    age= models.PositiveIntegerField(default=0)
    salary= models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    status = models.BooleanField(default=True)
    avatar= models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cvitae= models.ImageField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)


    def __str__(self):
        return self.names

    class Meta:
        verbose_name= 'Empleado'
        verbose_name_plural= 'Empleados'        
        dt_table= 'empleado'
        ordering=[id]