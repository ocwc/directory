from django import template
register = template.Library()

def show_facets(context, facet_object, facet_slug):
	return {'facet_slug': facet_slug,
			'facet_object': facet_object.get('fields').get(facet_slug)}

register.inclusion_tag('_single_facet.html', takes_context=True)(show_facets)