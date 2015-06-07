from django.conf.urls import patterns, include, url
from .views import cpu_view



urlpatterns = patterns('',

	url(r'^$' , 'apps.sistema.views.cpu_view'),
#	url(r'^$' , cpu_view.as_view()),
#	url(r'^memoria/$', BusquedaView.as_view()),
#	url(r'^disco/$', BusquedaAjaxView.as_view()),

)
