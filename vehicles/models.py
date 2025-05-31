from django.db import models
from customers.models import Customer



# Tabela do tipo de veículo:

class VehicleType(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,            # Normalização do dados, que seja o tipo único para não deixar duplicado
        verbose_name='Nome',

    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descrição'
    )

    create_at = models.DateTimeField(
        auto_now_add=True,             # Vai setar data e hora atual
        verbose_name='Criado em ',
    )

    update_at = models.DateTimeField(
        auto_now=True,                 # Armazena todas vez que for feito uma atualização e pega a data e hora
        verbose_name='Atualizado em ', 
    )

    class Meta:
        verbose_name = 'Tipo de Veículo'
        verbose_name_plural = 'Tipos de Veículos'

    def __str__(self):
        return self.name
    

# Tabela de veículos

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(
        VehicleType,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='vehicles',
        verbose_name='Tipo do Veículo',

    )

    license_plate = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Placa',

    )

    brand = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Marca'

    )

    model = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Modelo'
    
    )

    color = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Cor'

    )

    owner = models.ForeignKey(
        Customer,
        on_delete = models.PROTECT,
        blank=True,
        null=True,
        related_name='vehicles',
        verbose_name="Proprietário",
    )

    create_at = models.DateTimeField(
        auto_now_add=True,             # Vai setar data e hora atual
        verbose_name='Criado em ',
    )

    update_at = models.DateTimeField(
        auto_now=True,                 # Armazena todas vez que for feito uma atualização e pega a data e hora
        verbose_name='Atualizado em ', 
    )

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return self.license_plate


    
    
        

    