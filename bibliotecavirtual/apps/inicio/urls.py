from django.conf.urls import patterns, include, url
from .views import Registrarse, registro

urlpatterns = patterns('',

	url(r'^$' , 'django.contrib.auth.views.login',
		{'template_name':'inicio/index.html'}, name='login'),

	url(r'^cerrar/$' , 'django.contrib.auth.views.logout_then_login',
		 name='logout'),

	#url(r'^registrarse/$', Registrarse.as_view() , name = 'registrarse'),

	url(r'^registrarse/$', Registrarse , name = "registrarse"),
	#url(r'^registrarse/registro$', include('apps.inicio.views.registro' , namespace = "registro")),
	url(r'^registrarse/registro$', registro  , name= 'registro'),

	url(r'^autenticado/$' , 'django.contrib.auth.views.login',
		{'template_name':'inicio/autenticado.html'}, name='autenticado'),
)
																																																																																																																																																																																																			