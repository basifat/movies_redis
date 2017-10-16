from django.conf.urls import url, include
from .views import titles_view
from django.conf import settings


urlpatterns = [
    url(r'^$', titles_view),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns