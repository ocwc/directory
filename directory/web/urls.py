from django.conf.urls import patterns, include, url

from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet


from .views import IndexView, CustomFacetedSearchView

sqs = SearchQuerySet().facet('region')


urlpatterns = patterns('',
	url(r'^search/$', CustomFacetedSearchView(form_class=FacetedSearchForm, searchqueryset=sqs), name='haystack_search'),

	url(r'^$', IndexView.as_view(), name="index")
)