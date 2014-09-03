from django.core.management.base import BaseCommand

from web.models import Person

class Command(BaseCommand):
	help = "gathers emails from people inside directory"

	def handle(self, *args, **options):
		for p in Person.objects.all():
			print(p.email)