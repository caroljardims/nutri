from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'projeto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'cardapio.views.home', name='home'),
    url(r'^index/', 'cardapio.views.index', name='index'),
    # AUX
    url(r'^aux/', 'cardapio.views.aux', name='aux'),
    url(r'^addaux/', 'cardapio.views.addaux', name='addaux'),
    url(r'editaux/(?P<id_aux>\d+)/$', 'cardapio.views.editaux', name='editaux'),
    url(r'deleteaux/(?P<id_aux>\d+)/$', 'cardapio.views.deleteaux', name='deleteaux'),
    # ALIMENTOS
    url(r'^alimentos/', 'cardapio.views.alimentos', name='alimentos'),
    url(r'^addalimento/', 'cardapio.views.addalimento', name='addalimento'),
    url(r'deletealimento/(?P<id_alimentos>\d+)/$', 'cardapio.views.deletealimento', name='deletealimento'),
    url(r'editalimento/(?P<id_alimentos>\d+)/$', 'cardapio.views.editalimento', name='editalimento'),
    url(r'veralimento/(?P<id_alimentos>\d+)/$', 'cardapio.views.veralimento', name='veralimento'),
    # PREPARA
    url(r'^prepara/', 'cardapio.views.prepara', name='prepara'),
    url(r'^addprepara/', 'cardapio.views.addprepara', name='addprepara'),

 ]