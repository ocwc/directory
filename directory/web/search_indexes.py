import datetime

from haystack import indexes
from web.models import Person

class PersonIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    general_expertise = indexes.MultiValueField(faceted=True)
    oer_expertise = indexes.MultiValueField(faceted=True)
    openacess_expertise = indexes.MultiValueField(faceted=True)
    mooc_expertise = indexes.MultiValueField(faceted=True)
    
    region = indexes.MultiValueField(faceted=True)
    
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Person

    def prepare_general_expertise(self, obj):
        return [expertise.name for expertise in obj.general_expertise.all().order_by('name')]

    def prepare_oer_expertise(self, obj):
        return [expertise.name for expertise in obj.oer_expertise.all().order_by('name')]

    def prepare_openacess_expertise(self, obj):
        return [expertise.name for expertise in obj.openacess_expertise.all().order_by('name')]

    def prepare_mooc_expertise(self, obj):
        return [expertise.name for expertise in obj.mooc_expertise.all().order_by('name')]

    def prepare_region(self, obj):
        return [region.name for region in obj.region.all().order_by('name')]

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
