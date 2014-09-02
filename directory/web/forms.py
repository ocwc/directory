from django import forms
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, HTML, ButtonHolder
from crispy_forms.bootstrap import InlineRadios, InlineCheckboxes

from web.models import Person
from web.models import IS_MEMBER_CHOICES

class PersonCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        self.helper.form_class = 'form'
        self.helper.label_class = 'col-sm-12'
        self.helper.field_class = 'col-sm-8'

        self.fields['is_member'].choices = IS_MEMBER_CHOICES
        
        self.fields['general_expertise'].help_text = ''
        self.fields['oer_expertise'].help_text= ''
        self.fields['openacess_expertise'].help_text= ''
        self.fields['mooc_expertise'].help_text= ''
        self.fields['region'].help_text= ''

        self.helper.layout = Layout(
            Field('first_name'),
            Field('last_name'),
            Field('job_title'),
            Field('institution'),
            InlineRadios('is_member'),
        )

        self.helper.layout.append(Layout(
            Field('email'),
            Field('alternative_contact')
        ))

        self.helper.layout.append(Layout(
            Div(
                HTML("<h2>Languages</h2>"
                     "<p>Please list the language(s) in which you have speaking and writing proficiency at the following levels:</p>"),
                css_class='col-sm-10'),
            Field('language_native'),
            Field('language_business'),
            Field('language_conversational')
        ))

        self.helper.layout.append(Layout(
            Div(
                HTML("<h2>Areas of expertise</h2>"
                   "<p>Please indicate the areas of open education in which you have particular expertise. If you have experience, but not expertise, in certain areas, you may wish to mention these in personal statement, below.</p>"),
                css_class='col-sm-10'),
            InlineCheckboxes('general_expertise', template="bootstrap3/layout/checkboxselectmultiple_inline_fullwidth.html"),
            Field('general_expertise_other', css_class='col-sm-12')
        ))

        self.helper.layout.append(Layout(
            Div(
                HTML("<h2>Open Educational Resources</h2>"
                   "<p>Open Educational Resources refer to openly licensed content for educational purposes. This includes, but is not limited to, course materials, open textbooks, simulations, assessments, etc.</p>"),
                css_class='col-sm-10'),
            InlineCheckboxes('oer_expertise', template="bootstrap3/layout/checkboxselectmultiple_inline_fullwidth.html"),
            Field('oer_expertise_other', label="Other, please indicate:", css_class='col-sm-12')
        ))

        self.helper.layout.append(Layout(
            Div(HTML("<h2>Open Access</h2>"), css_class='col-sm-10'),
            InlineCheckboxes('openacess_expertise', template="bootstrap3/layout/checkboxselectmultiple_inline_fullwidth.html"),
            Field('openacess_expertise_other', css_class='col-sm-12')
        ))

        self.helper.layout.append(Layout(
            Div(HTML("<h2>Massive open online courses</h2>"), css_class='col-sm-10'),
            InlineCheckboxes('mooc_expertise', template="bootstrap3/layout/checkboxselectmultiple_inline_fullwidth.html"),
            Field('mooc_expertise_other', css_class='col-sm-12')
        ))

        self.helper.layout.append(Layout(
            Field('discipline'),
            InlineCheckboxes('region', template="bootstrap3/layout/checkboxselectmultiple_inline_fullwidth.html"),
            Field('personal_statement'),
            Field('external_links'),

            ButtonHolder(
                Submit('submit', 'Submit', css_class='col-sm-3'),
                css_class="col-sm-12"
            )
        ))

    def clean_email(self):
        data = self.cleaned_data['email']
        print(data)
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError(mark_safe('Profile with this email already exists. Please <a href="/directory/login/" class="btn btn-primary">Login</a> to edit your profile.'))

        return data
    
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'job_title', 'institution', 'is_member',
                    #'city', 'state_province', 'country',
                    'email', 'alternative_contact', 
                    'language_native', 'language_business', 'language_conversational', 
                    'general_expertise', 'general_expertise_other', 
                    'oer_expertise', 'oer_expertise_other', 
                    'openacess_expertise', 'openacess_expertise_other', 
                    'mooc_expertise', 'mooc_expertise_other', 
                    'discipline', 'region', 'personal_statement', 
                    'external_links', 
            )