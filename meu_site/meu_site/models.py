from django.db import models

class Funcionário(models.Model): 
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    
