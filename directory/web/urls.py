from django.conf.urls import patterns, url

# from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet
from haystack.views import FacetedSearchView

from .views import IndexView, PersonDetailView, DirectoryFacetedSearchForm

sqs = SearchQuerySet().facet('region').facet('general_expertise') \
		.facet('oer_expertise').facet('openacess_expertise').facet('mooc_expertise')

urlpatterns = patterns('',
	url(r'^search/$', FacetedSearchView(form_class=DirectoryFacetedSearchForm, searchqueryset=sqs), name='haystack_search'),
	url(r'^professional/(?P<slug>[\w-]+)/', PersonDetailView.as_view(), name="person-detail"),
	
	url(r'^$', IndexView.as_view(), name="index")
)