import xlrd
from optparse import make_option
from pprint import pprint as print

from django.core.management.base import BaseCommand

from web.models import Person

class Command(BaseCommand):
    help = "imports CSV created by Wordpress form"

    option_list = BaseCommand.option_list + (
        make_option('--file',
            action='store',
            dest='file',
            default=False,
            help='File to read from'),
        )

    def handle(self, *args, **options):
        if options.get('file'):
            self.import_form(filename=options.get('file'))

    def import_form(self, filename):
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_name('Sheet1')
        num_rows = sheet.nrows - 1

        curr_row = 0 # skip the header row
        while curr_row < num_rows:
            curr_row += 1
            row = sheet.row(curr_row)

            
