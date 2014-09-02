from django import template
register = template.Library()

def show_facets(context, facet_object, facet_slug):
    facet_object = facet_object.get('fields').get(facet_slug)
    facet_object.sort()

    return {'request': context.get('request'),
            'facet_slug': facet_slug,
            'facet_object': facet_object}

register.inclusion_tag('_single_facet.html', takes_context=True)(show_facets)

def is_facet_selected(context, facet_slug):
    selected_facets = context.get('request').GET.get('selected_facets', '')
    selected = False

    if "{0}_exact".format(facet_slug) in selected_facets or ":{0}".format(facet_slug) in selected_facets:
        selected = True
    
    return str(selected).lower()
    
register.simple_tag(takes_context=True)(is_facet_selected)