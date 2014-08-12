from vanilla import TemplateView
from haystack.views import FacetedSearchView

class IndexView(TemplateView):
	template_name = "index.html"


class CustomFacetedSearchView(FacetedSearchView):
    def extra_context(self):
        extra = super(CustomFacetedSearchView, self).extra_context()
        extra['results'] = self.results
        return extra
