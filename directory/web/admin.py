from django.contrib import admin

from web.models import GeneralExpertise, OERExpertise, OpenAccessExpertise, \
	MOOCExpertise, Region, Country, Person

class CountryAdmin(admin.ModelAdmin):
	list_filter = ('name', 'iso_code')

admin.site.register(GeneralExpertise)
admin.site.register(OERExpertise)
admin.site.register(OpenAccessExpertise)
admin.site.register(MOOCExpertise)
admin.site.register(Region)
admin.site.register(Country, CountryAdmin)
admin.site.register(Person)