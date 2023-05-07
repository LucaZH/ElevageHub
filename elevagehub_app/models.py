from django.db import models
from django.contrib.auth.models import User


class Animal(models.Model):
    nom = models.CharField(max_length=100)
    espece = models.CharField(max_length=100)
    date = models.DateField()
    poids_initial = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='media/images/animal_photos/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Activite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    type_activite = models.CharField(max_length=100)
    date_activite = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='media/images/activite_photos/', blank=True, null=True)


class Aliment(models.Model):
    nom = models.CharField(max_length=100)
    type_aliment = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/images/activite_photos/', blank=True, null=True)


class Stock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aliment = models.ForeignKey(Aliment, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    date_stock = models.DateTimeField()


class Croissance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    poids = models.DecimalField(max_digits=5, decimal_places=2)
    date_mesure = models.DateTimeField()
