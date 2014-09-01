from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, HTML
from crispy_forms.bootstrap import InlineRadios, InlineCheckboxes

from web.models import Person

class PersonCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-8'

        # TODO - Initial
        self.fields['is_member'].choices = ((1, 'Yes'), (0, 'No'), (2, "Don't know"))
        
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
            Div(HTML("<h2>Open Access</h2>")),
            InlineCheckboxes('openacess_expertise', template="bootstrap3/layout/checkboxselectmultiple_inline_fullwidth.html"),
            Field('openacess_expertise_other', css_class='col-sm-12')
        ))

        self.helper.layout.append(Layout(
            Div(HTML("<h2>MOOCs</h2>")),
            InlineCheckboxes('mooc_expertise', template="bootstrap3/layout/checkboxselectmultiple_inline_fullwidth.html"),
            Field('mooc_expertise_other', css_class='col-sm-12')
        ))

        self.helper.layout.append(Layout(
            Field('discipline'),
            InlineCheckboxes('region', template="bootstrap3/layout/checkboxselectmultiple_inline_fullwidth.html"),
            Field('personal_statement'),
            Field('external_links')
        ))

        self.helper.add_input(Submit('submit', 'Submit'))

    def save(self):
        # is_member fields

        pass
    
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