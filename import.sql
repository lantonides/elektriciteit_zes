copy temp(product,gasprijs_per_m3,prijs_per_kw,vastrecht_gas,vastrecht_elektriciteit,naam) from '/home/lo/zes/nrg.csv' delimiter ',' csv header; 

insert into bereken_kosten (product,gasprijs_per_m3,"prijs_per_Kw",vastrecht_gas,vastrecht_elektriciteit,leverancier_id) select product,gasprijs_per_m3,prijs_per_kW,vastrecht_gas,vastrecht_elektriciteit,naam from temp;

truncate temp;

