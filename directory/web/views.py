import datetime

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail

from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from vanilla import TemplateView, FormView, DetailView, CreateView, UpdateView

from haystack.forms import FacetedSearchForm
import loginurl.utils

from web.models import Person, GeneralExpertise, OERExpertise, OpenAccessExpertise, MOOCExpertise, Region
from web.forms import PersonCreateForm, LoginForm, PersonUpdateForm

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


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        user = User.objects.filter(email=email).first()

        expires = datetime.datetime.now() + datetime.timedelta(days=7)
        key = loginurl.utils.create(user, usage_left=None, expires=expires)

        url = 'https://www.oeconsortium.org/directory/login/{0}'.format(key.key)

        body = render_to_string('login_mail_body.txt', {'url': url})
        subject = render_to_string('login_mail_subject.txt')
        send_mail(subject, body, 'memberservices@oeconsortium.org', [email])

        return render(self.request, "login_emailsent.html")

class DirectoryFacetedSearchForm(FacetedSearchForm):
    def no_query_found(self):
        return self.searchqueryset.all()

class PersonDetailView(DetailView):
    model = Person
    template_name = "person_detail.html"
    lookup_field = 'slug'
    context_object_name = 'person'

class PersonCreateView(AnonymousRequiredMixin, CreateView):
    model = Person
    form_class = PersonCreateForm

    def form_valid(self, *args, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, 
            'Thank you for adding your profile to The Open Education Professional Directory. '
            'To edit it, you will have to first <a href="/directory/login/" class="btn btn-primary">Login</a>'
        )

        return super().form_valid(*args, **kwargs)

class PersonUpdateView(LoginRequiredMixin, UpdateView):
    model = Person
    form_class = PersonUpdateForm

    def get_object(self):
        person = Person.objects.filter(user=self.request.user).first()
        if not person:
            raise ObjectDoesNotExist('Your profile does not exist')

        return person

    # def get_form(self, data=None, files=None, **kwargs):
    # #     kwargs['initial'] = self.get_object()

    #     return self.get_form_class()(data, files, **kwargs)
