from django.db import models

class GeneralExpertise(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class OERExpertise(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class OpenAccessExpertise(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class MOOCExpertise(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Region(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Address(models.Model):
	street_address = models.CharField(max_length=255, blank=True)
	street_address2 = models.CharField(max_length=255, blank=True)
	city = models.CharField(max_length=255, blank=True)
	state_province = models.CharField(max_length=255, blank=True)
	zip_postal = models.CharField(max_length=255, blank=True)
	country = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.country

class Person(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)

	slug = models.SlugField(max_length=255)

	job_title = models.CharField(max_length=255, blank=True)
	institution = models.CharField(max_length=255, blank=True)
	is_member = models.NullBooleanField(default=None,
										verbose_name=u'Open Education Consortium member?')
	address = models.ForeignKey(Address, null=True)

	email = models.CharField(max_length=255)
	alternative_contact = models.CharField(max_length=255, blank=True)

	language_native = models.TextField(blank=True, verbose_name=u'Native/near native level')
	language_business = models.TextField(blank=True, verbose_name=u'Business level')
	language_conversational = models.TextField(blank=True, verbose_name=u'Conversational')

	general_expertise = models.ManyToManyField(GeneralExpertise, null=True, verbose_name=u'Open Education - General')
	general_expertise_other = models.TextField(max_length=255, blank=True, verbose_name=u'Other, please indicate')

	oer_expertise = models.ManyToManyField(OERExpertise, null=True, verbose_name=u'Open Educational Resources')
	oer_expertise_other = models.TextField(blank=True, verbose_name=u'Other, please indicate:')

	openacess_expertise = models.ManyToManyField(OpenAccessExpertise, null=True, verbose_name=u'MOOCs')
	openacess_expertise_other = models.TextField(blank=True, verbose_name=u'Other, please indicate:')

	mooc_expertise = models.ManyToManyField(MOOCExpertise, null=True, 
		verbose_name=u'If you have expertise with open education in a particular discipline, please indicate:')
	mooc_expertise_other = models.TextField(blank=True)

	discipline = models.TextField(blank=True, 
		verbose_name=u'If you have expertise with open education in a particular discipline, please indicate:')

	region = models.ManyToManyField(Region, 
		verbose_name=u'Please select the geographic regions in which you have professional experience:*')

	personal_statement = models.TextField(blank=True)
	external_links = models.TextField(blank=True)

	pub_date = models.DateTimeField(auto_now_add=True)
	mod_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return u"{0} {1}".format(self.first_name, self.last_name)
