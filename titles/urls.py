from django.conf.urls import url, include
from .views import titles_view


urlpatterns = [
    url(r'^$', titles_view),
]

