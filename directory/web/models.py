from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

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

class Country(models.Model):
    name = models.CharField(max_length=255)
    iso_code = models.CharField(max_length=6)

    def __str__(self):
        return self.name

IS_MEMBER_CHOICES = (
    ('0', "Don't know"),
    ('1', "Yes"),
    ('2', "No")
)

class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    user = models.ForeignKey(User, null=True)

    email = models.EmailField(max_length=255)
    alternative_contact = models.CharField(max_length=255, blank=True)

    slug = models.SlugField(max_length=255)

    job_title = models.CharField(max_length=255, blank=True)
    institution = models.CharField(max_length=255, blank=True)
    is_member = models.CharField(max_length=10,
                                    choices=IS_MEMBER_CHOICES,
                                    verbose_name=u'Open Education Consortium member?')

    city = models.CharField(max_length=255, blank=True)
    state_province = models.CharField(max_length=255, blank=True)
    country = models.ForeignKey(Country, null=True)

    language_native = models.TextField(blank=True, verbose_name=u'Native/near native level')
    language_business = models.TextField(blank=True, verbose_name=u'Business level')
    language_conversational = models.TextField(blank=True, verbose_name=u'Conversational')

    general_expertise = models.ManyToManyField(GeneralExpertise, null=True, blank=True, verbose_name=u'Open Education - General')
    general_expertise_other = models.TextField(max_length=255, blank=True, verbose_name=u'Other, please indicate:')

    oer_expertise = models.ManyToManyField(OERExpertise, null=True, blank=True, verbose_name=u'Open Educational Resources')
    oer_expertise_other = models.TextField(blank=True, verbose_name=u'Other, please indicate:')

    openacess_expertise = models.ManyToManyField(OpenAccessExpertise, blank=True, null=True, verbose_name=u'Open Access')
    openacess_expertise_other = models.TextField(blank=True, verbose_name=u'Other, please indicate:')

    mooc_expertise = models.ManyToManyField(MOOCExpertise, blank=True, null=True, verbose_name=u'MOOCs')
    mooc_expertise_other = models.TextField(blank=True, verbose_name=u'Other, please indicate:')

    discipline = models.TextField(blank=True, 
        verbose_name=u'If you have expertise with open education in a particular discipline, please indicate:')

    region = models.ManyToManyField(Region, 
        verbose_name=u'Please select the geographic regions in which you have professional experience:')

    personal_statement = models.TextField(blank=True)
    external_links = models.TextField(blank=True)

    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)

    visible = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            next = 0
            while (not self.slug) or (Person.objects.filter(slug=self.slug).exists()):
                self.slug = slugify("{0} {1}".format(self.first_name, self.last_name))
                
                if next:
                    self.slug += '-{0}'.format(next)
                next += 1

        if not self.user:
            User.objects.get_or_create(
                email = self.email,
                defaults = {
                    'username': self.slug[:30],
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'is_active': True
                }
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return u"{0} {1}".format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('directory:person-detail', args={self.slug})
