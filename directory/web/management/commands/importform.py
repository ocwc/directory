import xlrd
from optparse import make_option
# from pprint import pprint as print

from django.core.management.base import BaseCommand

from web.models import Person, Address, GeneralExpertise, OERExpertise, OpenAccessExpertise, MOOCExpertise, Region

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
        Person.objects.all().delete()

        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_name('Sheet1')
        num_rows = sheet.nrows - 1

        curr_row = 0 # skip the header row
        while curr_row < num_rows:
            curr_row += 1
            row = sheet.row(curr_row)

            address = Address.objects.create(
                street_address = row[5].value, #  5 - Address (Street Address)
                street_address2 = row[6].value, #  6 - Address (Address Line 2)
                city = row[7].value,            #  7 - Address (City)
                state_province = row[8].value,  #  8 - Address (State / Province)
                zip_postal = row[9].value,      #  9 - Address (ZIP / Postal Code)
                country = row[10].value         # 10 - Address (Country)
            )

            person, is_created = Person.objects.get_or_create(
                    email = row[11].value,       # 11 - Email
                    defaults = dict(
                        first_name = row[0].value,   #  0 - Name (First)
                        last_name = row[1].value,    #  1 - Name (Last)
                        job_title = row[2].value,    #  2 - Job Title
                        institution = row[3].value,  #  3 - Institution

                        alternative_contact = row[12].value, # 12 - Alternative contact

                        language_native = row[13].value,    # 13 - Native/near native level
                        language_business = row[14].value,  # 14 - Business level
                        language_conversational = row[15].value # 15 - Conversational
                )
            )
            person.address = address

            is_member_value = row[4].value  #  4 - Open Education Consortium member?
            if is_member_value == 'Yes':
                is_member = True
            elif is_member_value == 'No':
                is_member = False
            else:
                is_member = None

            person.is_member = is_member
            person.save()

            # 16 - Oversight of open education at an institution
            # 17 - Open Education policy development
            # 18 - Implementation of open education policies
            # 19 - Open licenses
            # 20 - Business Models for open education
            # 21 - Fundraising for open education projects
            # 22 - Research in open education
            # 23 - Accessibility in open education
            # 24 - Assessment and accreditation of learning through open education
            # 25 - Awareness raising and outreach
            for col in range(16, 26):
                val = row[col].value
                if val:
                    try:
                        expertise = GeneralExpertise.objects.get(name=val)
                        person.general_expertise.add(expertise)
                    except GeneralExpertise.DoesNotExist:
                        pass
            person.oer_expertise_other = row[26].value

            # 27 - Authoring OER
            # 28 - Using/remixing OER for face to face education
            # 29 - Using/remixing OER for online education
            # 30 - OER project management
            # 31 - Instructional design using OER
            # 32 - Peer review of OER
            # 33 - Faculty adoption of OER
            # 34 - Libraries and OER
            # 35 - Technology for OER
            # 36 - OER and workforce development
            # 37 - OER and lifelong learning
            for col in range(27, 38):
                val = row[col].value
                if val:
                    try:
                        expertise = OERExpertise.objects.get(name=val)
                        person.oer_expertise.add(expertise)
                    except OERExpertise.DoesNotExist:
                        pass
            person.oer_expertise_other = row[38].value

            # 39 - Open Access policy development
            # 40 - Open Access project management
            # 41 - Open Access publishing
            # 42 - Peer review in open access journals
            # 43 - Implementation of open access practices
            for col in range(39, 44):
                val = row[col].value
                if val:
                    try:
                        expertise = OpenAccessExpertise.objects.get(name=val)
                        person.openacess_expertise.add(expertise)
                    except OpenAccessExpertise.DoesNotExist:
                        pass
            person.openacess_expertise_other = row[44].value

            # 45 - Authoring MOOCs
            # 46 - Facilitating MOOCs
            # 47 - MOOC instructional design
            # 48 - Openly licensed content in MOOCs
            # 49 - Technology for MOOCs
            # 50 - Overall project management for MOOC development
            # 51 - Using MOOCs in formal education programs
            for col in range(45, 52):
                val = row[col].value
                if val:
                    try:
                        expertise = MOOCExpertise.objects.get(name=val)
                        person.mooc_expertise.add(expertise)
                    except MOOCExpertise.DoesNotExist:
                        pass
            person.mooc_expertise_other = row[52].value

            person.discipline = row[53].value # 53 - If you have expertise with open education in a particular discipline, please indicate:

            # 54 - Africa
            # 55 - Asia/Pacific
            # 56 - Europe
            # 57 - North America
            # 58 - South America
            for col in range(54, 59):
                val = row[col].value
                if val:
                    try:
                        expertise = Region.objects.get(name=val)
                        person.region.add(expertise)
                    except Region.DoesNotExist:
                        pass

            person.personal_statement = row[59].value   #  59 - Personal statement
            person.external_links = row[60].value       #  60 - External links

            person.save()

