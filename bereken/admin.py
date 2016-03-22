from django.contrib import admin
from .models import Kosten,Leveranciers,Netbeheerders,Netbeheerderkosten,Algemenekosten,Regiotoeslag

from import_export import resources, fields, widgets
from import_export.admin import ImportExportModelAdmin,ImportMixin

# Register your models here.

class KostenResource(resources.ModelResource):
	leverancier=fields.Field(column_name='naam',attribute='leverancier',widget=widgets.ForeignKeyWidget(Leveranciers,'naam'))	
	class Meta:
		model=Kosten

class KostenAdmin(ImportMixin,admin.ModelAdmin):
	resource_class=KostenResource

class LeveranciersResource(resources.ModelResource):
	class Meta:
		model=Leveranciers
		import_id_fields=['naam']

class LeveranciersAdmin(ImportMixin,admin.ModelAdmin):
	resource_class=LeveranciersResource

admin.site.register(Leveranciers,LeveranciersAdmin)
admin.site.register(Netbeheerders)
admin.site.register(Netbeheerderkosten)
admin.site.register(Algemenekosten)
admin.site.register(Regiotoeslag)
admin.site.register(Kosten,KostenAdmin)
