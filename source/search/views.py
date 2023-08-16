from django.shortcuts import render

from .search import lookup


def search_view(request):
    query_paramater = request.GET.get('q')

    context = {}

    if query_paramater:
        results = lookup(query_paramater)
        context['results'] = results
        context['query'] = query_paramater

    return render(request, 'search.html', context) 

    