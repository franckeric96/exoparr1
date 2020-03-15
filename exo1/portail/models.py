from django.db import models

# Create your models here.
class Service(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/Service')
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.nom
    
class Season(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/Season')
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Season'
        verbose_name_plural = 'Seasons'

    def __str__(self):
        return self.nom
    
    
class Gallerie(models.Model):
    titre = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/Gallerie')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Gallerie'
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return self.titre
    