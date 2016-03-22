from django import forms
from .models import Leveranciers,Netbeheerders,Netbeheerderkosten,Kosten

class InvulForm(forms.Form):
#        leverancier=forms.ModelChoiceField(label='Wie is uw leverancier?',queryset=Leveranciers.objects.all())
        netbeheerder=forms.ModelChoiceField(label='Wie is uw netbeheerder?',queryset=Netbeheerders.objects.all())
	huidig_pijs_kw=forms.CharField(label='Wat is uw huidige energieprijsprijs per Kwh?', max_length=10)
	huidig_prijs_m3=forms.CharField(label='Wat is uw huidige gasprijs per m3?', max_length=10)
        gasverbruik=forms.CharField(label='Wat is uw huidige gasverbruik in m3 per jaar?', max_length=10)
        kw_verbruik=forms.CharField(label='Wat is uw huidige elektriciteitsverbruik in Kwh per jaar?',max_length=10)

