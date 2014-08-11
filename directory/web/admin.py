from django.contrib import admin

from web.models import GeneralExpertise, OERExpertise, OpenAccessExpertise, \
	MOOCExpertise, Region, Address, Person

admin.site.register(GeneralExpertise)
admin.site.register(OERExpertise)
admin.site.register(OpenAccessExpertise)
admin.site.register(MOOCExpertise)
admin.site.register(Region)
admin.site.register(Address)
admin.site.register(Person)