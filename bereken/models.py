from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Leveranciers(models.Model):
        naam=models.CharField(max_length=35,primary_key=True)

        def __str__(self):
                return(self.naam)

class Netbeheerders(models.Model):
        naam=models.CharField(max_length=35)

        def __str__(self):
                return(self.naam)

class Kosten(models.Model):
        product=models.CharField(max_length=50)
	gasprijs_per_m3=models.FloatField()
        prijs_per_Kw=models.FloatField()
	vastrecht_gas=models.FloatField()
	vastrecht_elektriciteit=models.FloatField()
	leverancier=models.ForeignKey(Leveranciers, on_delete=models.CASCADE, default=0)
	datum=models.DateTimeField(default=timezone.now)
	def __str__(self):
                return str(self.product)

class Regiotoeslag(models.Model):
	jaar=models.CharField(max_length=4)
	regio_1=models.FloatField()
	regio_2=models.FloatField()
	regio_3=models.FloatField()
        regio_4=models.FloatField()
        regio_5=models.FloatField()
        regio_6=models.FloatField()
        regio_7=models.FloatField()
        regio_8=models.FloatField()
        regio_9=models.FloatField()
        regio_10=models.FloatField()
	leverancier=models.ForeignKey(Leveranciers, on_delete=models.CASCADE, default=0)

	def __str__(self):
                return str(self.leverancier)

class Netbeheerderkosten(models.Model):
        capaciteitstarief_elektriciteit_25A_onbemeten_per_jaar=models.FloatField()
        capaciteitstarief_elektriciteit_25A_bemeten_per_jaar=models.FloatField()
        capaciteitstarief_gas=models.FloatField()
        netbeheerder=models.ForeignKey(Netbeheerders, on_delete=models.CASCADE, default=0)

        def __str__(self):
                return str(self.netbeheerder)

class Algemenekosten(models.Model):
        ODE_per_kw_inclBTW=models.FloatField()
        ODE_per_m3_inclBTW=models.FloatField()
        energiebelasting_per_kw_inclBTW=models.FloatField()
        energiebelasting_per_m3_inclBTW=models.FloatField()
        BTW=models.FloatField(max_length=10)
        heffingskorting_elektriciteit=models.FloatField()
        jaar=models.CharField(max_length=4)

        def __str__(self):
                return(self.jaar)
