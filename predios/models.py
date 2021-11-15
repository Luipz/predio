from django.db import models

class Usuarios(models.Model):

    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


    def __str__(self):

        return self.name, self.last_name


class Predio(models.Model):

    car_brand = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=100)
    #notes = models.TextField()
    usuarios = models.ForeignKey(
        Usuarios, related_name="predios", on_delete=models.CASCADE
    )
    def __str__(self):

        return self.car_brand, self.license_plate