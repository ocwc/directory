from django.conf.urls import patterns, url

from loginurl.views import cleanup, login

from haystack.query import SearchQuerySet
from haystack.views import FacetedSearchView

from .views import IndexView, PersonDetailView, PersonCreateView, DirectoryFacetedSearchForm, \
	LoginView

sqs = SearchQuerySet().facet('region').facet('general_expertise') \
		.facet('oer_expertise').facet('openacess_expertise').facet('mooc_expertise')

urlpatterns = patterns('',
    url(r'^login/cleanup/$', cleanup, name='loginurl-cleanup'),
    url(r'^login/(?P<key>[0-9A-Za-z]+-[a-z0-9-]+)/$', login, name='loginurl-login'), 
	url(r'^login/$', LoginView.as_view(), name='login'),

	url(r'^search/$', FacetedSearchView(form_class=DirectoryFacetedSearchForm, searchqueryset=sqs), name='haystack_search'),
	url(r'^professional/(?P<slug>[\w-]+)/', PersonDetailView.as_view(), name="person-detail"),

	url(r'^add/$', PersonCreateView.as_view(), name="person-create"),
	
	url(r'^$', IndexView.as_view(), name="index")
)