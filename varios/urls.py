from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('app1.urls', namespace='app1')),
    url(r'^app2/', include('app2.urls', namespace='app2')),
]
