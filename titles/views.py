from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from titles.services import get_titles_with_cache as get_titles
#from .services import get_recipes_without_cache as get_recipes

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

@cache_page(CACHE_TTL)
def titles_view(request):
    return render(request, 'titles/movie_title.html', {
        'titles': get_titles()
    })
