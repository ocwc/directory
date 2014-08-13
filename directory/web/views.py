from vanilla import TemplateView, DetailView

from haystack.forms import FacetedSearchForm

from web.models import Person

class IndexView(TemplateView):
    template_name = "index.html"

class DirectoryFacetedSearchForm(FacetedSearchForm):
    def no_query_found(self):
        return self.searchqueryset.all()

class PersonDetailView(DetailView):
	model = Person
	template_name = "person_detail.html"
	lookup_field = 'slug'
	context_object_name = 'person'