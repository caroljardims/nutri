from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'projeto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'cardapio.views.home', name='home'),
    url(r'^index/', 'cardapio.views.index', name='index'),
    url(r'^aux/', 'cardapio.views.aux', name='aux'),
    url(r'^addaux/', 'cardapio.views.addaux', name='addaux'),

 ]