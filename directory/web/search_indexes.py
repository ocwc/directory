import datetime

from haystack import indexes
from web.models import Person

class PersonIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    # first_name = indexes.CharField(model_attr="first_name")
    # last_name = indexes.CharField(model_attr="last_name")
    # job_title = indexes.CharField(model_attr="job_title")
    # institution = indexes.CharField(model_attr="institution")

    # general_expertise = indexes.CharField(model_attr="general_expertise__name")
    # general_expertise = indexes.MultiValueField()
    # general_expertise_other = indexes.CharField(model_attr="general_expertise_other")
    # oer_expertise = indexes.CharField(model_attr="oer_expertise")
    # oer_expertise_other = indexes.CharField(model_attr="oer_expertise_other")
    # openacess_expertise = indexes.CharField(model_attr="openacess_expertise")
    # openacess_expertise_other = indexes.CharField(model_attr="openacess_expertise_other")
    # mooc_expertise = indexes.CharField(model_attr="mooc_expertise")
    # mooc_expertise_other = indexes.CharField(model_attr="mooc_expertise_other")
    
    discipline = indexes.CharField(model_attr="discipline")
    region = indexes.MultiValueField(faceted=True)
    
    # personal_statement = indexes.CharField(model_attr="personal_statement")
    # external_links = indexes.CharField(model_attr="external_links")

    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Person

    def prepare_region(self, obj):
        return [region.name for region in obj.region.all().order_by('name')]

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
