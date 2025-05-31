from django.db.models.signals import post_save
from django.dispatch import receiver

from parking.models import ParkingRecord


#Essa função vai desparar sempre que acontecer um post_save, ou seja, quando salvar um registro ou editar e salvar o banco

@receiver(post_save, sender=ParkingRecord)  #Receber eventos
def upadate_parking_spot_status(sender, instance, created, **kwargs):
    parking_spot = instance.parking_spot
    parking_spot.is_occupied = (instance.exit_time is None)
    parking_spot.save()