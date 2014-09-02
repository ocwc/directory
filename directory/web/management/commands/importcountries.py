from optparse import make_option

from django.core.management.base import BaseCommand

from web.models import Country

class Command(BaseCommand):
    help = "imports TXT of countries copied from http://en.wikipedia.org/wiki/ISO_3166-1#Officially_assigned_code_elements"

    option_list = BaseCommand.option_list + (
        make_option('-f', '--file',
            action='store',
            dest='file',
            default=False,
            help='File to read from'),
        )

    def handle(self, *args, **options):
        if options.get('file'):
            self.import_countries(filename=options.get('file'))

    def import_countries(self, filename):
        f = open(filename)
        for line in f.readlines()[1:]:
            country_name, iso_code = line.split('\t')[0:2]


            Country.objects.get_or_create(name=country_name, iso_code=iso_code)
        self.stdout.write("Done. %s countries imported " % Country.objects.count())
