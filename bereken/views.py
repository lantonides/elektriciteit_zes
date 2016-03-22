from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import InvulForm
from .models import Netbeheerderkosten,Kosten,Algemenekosten, Regiotoeslag
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import datetime
from django.db.models import Avg

def bereken(request):
        if request.method=='POST':
                form=InvulForm(request.POST)
                if form.is_valid():
			huidig_pijs_kw=form.cleaned_data['huidig_pijs_kw']
			huidig_prijs_m3=form.cleaned_data['huidig_prijs_m3']
                        gasverbruik=form.cleaned_data['gasverbruik']
                        kw_verbruik=form.cleaned_data['kw_verbruik']
			netbeheerder=form.cleaned_data['netbeheerder']
                        heffingskorting=Algemenekosten.objects.get(jaar='2016').heffingskorting_elektriciteit
                        capaciteitstarief_elektriciteit_25A=Netbeheerderkosten.objects.get(netbeheerder=netbeheerder).capaciteitstarief_elektriciteit_25A_bemeten_per_jaar
                        capaciteitstarief_gas=Netbeheerderkosten.objects.get(netbeheerder=netbeheerder).capaciteitstarief_gas

			totaal_elektriciteitskosten=float(kw_verbruik)*float(huidig_pijs_kw)+capaciteitstarief_elektriciteit_25A-heffingskorting
                        totaal_gaskosten=float(gasverbruik)*float(huidig_prijs_m3)+capaciteitstarief_gas
			
                        jaar=[]
                        jaarkosten_gas=[]
                        jaarkosten_el=[]
                        jg=totaal_gaskosten
                        je=totaal_elektriciteitskosten
                        for x in range(0,25):
                                jaarkosten_gas1=jg*x
                                jaarkosten_el1=je*x
                                jaar.append(x)
                                jaarkosten_gas.append(jaarkosten_gas1)
                                jaarkosten_el.append(jaarkosten_el1)

                        plt.clf()
                        plt.plot(jaar,jaarkosten_el,label='Huidige elektriciteits situatie')
                        plt.plot(jaar,jaarkosten_gas,label='Huidige gas situatie')

                        plt.ylabel('Euro')
                        plt.xlabel('Jaren')

                        lgd = plt.legend(loc='upper center', bbox_to_anchor=(0.5,-0.1))
                        plt.title('Energie kosten')

                        buf = BytesIO()
                        plt.savefig(buf, format='png', bbox_extra_artists=(lgd,),bbox_inches='tight')
                        out = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
                        img_tag = "data:image/png;base64,{0}".format(out)
                        buf.close()

                        return render(request,'bereken/resultaat.html',{'gasverbruik':gasverbruik, 'kw_verbruik':kw_verbruik,'heffingskorting':heffingskorting,'capaciteitstarief_elektriciteit_25A':capaciteitstarief_elektriciteit_25A,'capaciteitstarief_gas':capaciteitstarief_gas,'img_tag':img_tag,'totaal_elektriciteitskosten':totaal_elektriciteitskosten,'totaal_gaskosten':totaal_gaskosten,'netbeheerder':netbeheerder})

        else:
                form=InvulForm()
        return render(request, 'bereken/invul.html',{'form':form})

def gasregios(request):
	gasregios=Regiotoeslag.objects.all
	return render(request,'bereken/gasregios.html',{'gasregios':gasregios})

def tarieven(request):
	enddate=datetime.date.today()
	startdate=enddate-datetime.timedelta(days=30)
	tarieven=Kosten.objects.filter(datum__range=[startdate,enddate])
	return render(request,'bereken/tarieven.html',{'tarieven':tarieven})

def prijsontwikkeling(request):
	gem_gasprijs=Kosten.objects.all().aggregate(Avg('gasprijs_per_m3')).get('gasprijs_per_m3__avg',0.00)
	gem_kwprijs=Kosten.objects.all().aggregate(Avg('prijs_per_Kw')).get('prijs_per_Kw__avg',0.00)
	
	gem_kwprijs2=Kosten.objects.filter(datum__year='2016').extra({'day' : "DAY(datum)"}).values_list('day').aggregate(Avg('prijs_per_Kw'))

	
	
	return render(request,'bereken/prijsontwikkeling.html',{'gem_gasprijs':gem_gasprijs,'gem_kwprijs':gem_kwprijs,'gem_kwprijs2':gem_kwprijs2})
