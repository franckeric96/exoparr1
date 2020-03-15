from django.db import models

# Create your models here.
class SocialAccount(models.Model):
    ICONS = [
        ("Facebook", "fa-facebook"),
        ("twitter", "fa-twitter"),
        ("Instagram", "fa-instagram"),

        
    ]
    
    nom = models.CharField(max_length=255)
    icon = models.CharField(choices=ICONS, max_length=20)
    lien = models.URLField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Social Account'
        verbose_name_plural = 'Social Accounts'

    def __str__(self):
        return self.nom
    
    
class InfoSite(models.Model):
    
    titre = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/InfoSite")
    lien = models.URLField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Info Site'
        verbose_name_plural = 'Info Sites'

    def __str__(self):
        return self.titre
    
    
class Temoignage(models.Model):
    
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/Temoignage")
    message = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Temoignage'
        verbose_name_plural = 'Temoignages'

    def __str__(self):
        return self.nom