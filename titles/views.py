from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.views.decorators.cache import cache_page
#from titles.services import get_title_with_cache as get_titles
from titles.services import get_title_without_cache as get_titles

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
#
@cache_page(CACHE_TTL)
def titles_view(request):
    title2 = get_titles()
    return render(request, 'titles/movie_title.html', {
        'titles': get_titles()
    })
