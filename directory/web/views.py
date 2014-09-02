from django.contrib import messages

from vanilla import TemplateView, DetailView, CreateView

from haystack.forms import FacetedSearchForm

from web.models import Person, GeneralExpertise, OERExpertise, OpenAccessExpertise, MOOCExpertise, Region
from web.forms import PersonCreateForm

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['general_expertise'] = GeneralExpertise.objects.all().order_by('name')
        context['oer_expertise'] = OERExpertise.objects.all().order_by('name')
        context['openacess_expertise'] = OpenAccessExpertise.objects.all().order_by('name')
        context['mooc_expertise'] = MOOCExpertise.objects.all().order_by('name')
        context['region'] = Region.objects.all().order_by('name')

        return context

class DirectoryFacetedSearchForm(FacetedSearchForm):
    def no_query_found(self):
        return self.searchqueryset.all()

class PersonDetailView(DetailView):
    model = Person
    template_name = "person_detail.html"
    lookup_field = 'slug'
    context_object_name = 'person'

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonCreateForm

    def form_valid(self, *args, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, 
            'Thank you for adding your profile to The Open Professionals Directory. '
            'To edit it, you will have to first <a href="/directory/login/" class="btn btn-primary">Login</a>'
        )

        return super().form_valid(*args, **kwargs)