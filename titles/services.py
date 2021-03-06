from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from .models import Titles

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def get_title_without_cache():
    return list(Titles.objects.all())


def get_title_with_cache():
    if 'titles' in cache:
        titles = cache.get('titles')
    else:
        titles = list(Titles.objects.all())
        cache.set('titles', titles, timeout=CACHE_TTL)
    return titles
