from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',


    
    #INICIO
    url(r'^' , include('apps.inicio.urls', namespace='inicio')),

    #AUTORES
    url(r'^autor/' , include('apps.autores.urls')),

    #LIBROS
    url(r'^libros/' , include('apps.libros.urls')),

    url(r'^sistema/' , include('apps.sistema.urls', namespace='sistema')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': settings.MEDIA_ROOT, } ),


)
