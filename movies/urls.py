
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns +=[
    url(r'^titles/', include('titles.urls'))
]
