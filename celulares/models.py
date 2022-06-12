from django.db import models
from django.urls import reverse


class Celular(models.Model):
    nombre = models.CharField(max_length=200)
    materiales = models.FloatField(default=0)
    uso_energia = models.FloatField(default=0)
    bateria = models.FloatField(default=0)
    final_vida = models.FloatField(default=0)
    embalaje = models.FloatField(default=0)
    corporativo = models.FloatField(default=0)
    fabricacion = models.FloatField(default=0)

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('celular-detail', args=[str(self.id)])

    def get_edit_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('editar_celular', args=[str(self.id)])

    def general(self):
        return (self.materiales + self.uso_energia + self.bateria + self.final_vida + self.embalaje + self.corporativo
                + self.fabricacion)/7
