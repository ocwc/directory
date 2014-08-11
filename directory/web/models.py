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
		return self.name

class Person(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	job_title = models.CharField(max_length=255, blank=True)
	institution = models.CharField(max_length=255, blank=True)
	is_member = models.NullBooleanField(default=None)
	address = models.ForeignKey(Address, null=True)

	email = models.CharField(max_length=255)
	alternative_contact = models.CharField(max_length=255, blank=True)

	language_native = models.TextField(blank=True)
	language_business = models.TextField(blank=True)
	language_conversational = models.TextField(blank=True)

	general_expertise = models.ManyToManyField(GeneralExpertise, null=True)
	general_expertise_other = models.CharField(max_length=255, blank=True)

	oer_expertise = models.ManyToManyField(OERExpertise, null=True)
	oer_expertise_other = models.CharField(max_length=255, blank=True)

	openacess_expertise = models.ManyToManyField(OpenAccessExpertise, null=True)
	openacess_expertise_other = models.CharField(max_length=255, blank=True)

	mooc_expertise = models.ManyToManyField(MOOCExpertise, null=True)
	mooc_expertise_other = models.CharField(max_length=255, blank=True)

	discipline = models.CharField(max_length=255, blank=True)

	region = models.ManyToManyField(Region)

	personal_statement = models.TextField(blank=True)
	external_links = models.TextField(blank=True)

	pub_date = models.DateTimeField(auto_now_add=True)
	mod_date = models.DateTimeField(auto_now=True)