from django.views.generic import TemplateView,FormView
from .forms import UserForm
from django.core.urlresolvers import reverse_lazy
from .models import usuario, Perfiles
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt
from django.shortcuts import render # Create your views here.


@csrf_exempt
@xframe_options_exempt

def Registrarse(request):
	return render(request, 'inicio/registrarse.html')

@csrf_exempt
@xframe_options_exempt

def registro(request):

	#	form_class = UserForm

		user= request.POST['username']
		print user
		return render(request, 'inicio/registrarse.html')



		'''def form_valid(self, form):
			user = form.save()
			perfil = usuario()
			#print user
			perfil.username = user
			perfil.nombre = form.cleaned_data['nombre']
			perfil.apellido = form.cleaned_data['apellido']
			#perfil.email = form.cleaned_data['nombre']

			print perfil.username,perfil.nombre,perfil.apellido
			#perfil.save()
			return super(Registrarse , self).form_valid(form)
'''

'''
# Esto es con clases pero lo de abajo le anula por ende hago sin clases
@csrf_exempt
@xframe_options_exempt
class Registrarse(FormView):
	template_name = 'inicio/registrarse.html'
	form_class = UserForm
	success_url = reverse_lazy('registrarse')


	def form_valid(self, form):
		user = form.save()
		perfil = usuario()
		#print user
		perfil.username = user
		perfil.nombre = form.cleaned_data['nombre']
		perfil.apellido = form.cleaned_data['apellido']
		#perfil.email = form.cleaned_data['nombre']

		print perfil.username,perfil.nombre,perfil.apellido
		#perfil.save()
		return super(Registrarse , self).form_valid(form)
'''
'''
		if libros:
			datos = []
			for libro in libros:
				autores = libro.autor.all()
				datos.append(dict([(libro,autores)]))
			return render(request,'libros/buscar.html',
					 {'datos':datos})
		else:
			autores = Autor.objects.filter(nombre__contains=buscar)
			return render(request, 'libros/buscar.html',
						{'autores':autores , 'autor':True})
'''


'''
class Registrarse(FormView):
	template_name = 'inicio/registrarse.html'
	form_class = UserForm
	success_url = reverse_lazy('registrarse')

	def form_valid(self, form):
		user = form.save()
		perfil = Perfiles()
		perfil.usuario = user
		perfil.telefono = form.cleaned_data['telefono']
		perfil.save()
		return super(Registrarse , self).form_valid(form)
'''