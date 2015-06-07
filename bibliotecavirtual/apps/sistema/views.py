from django.views.generic import TemplateView,ListView
#from .models import Libro
#from apps.autores.models import Autor
from django.shortcuts import render # Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
import psutil

'''
class cpu_view(TemplateView):
	
	def post(self, request, *args, **kwargs):
		cpu= psutil.virtual_memory()
		print cpu
		return render(request, 'sistema/cpu.html', {'cpu':cpu}) ## este es para tener los estilos 
		#return render_to_response('sistema/cpu.html', context_instance = RequestContext(request))
'''


def cpu_view(request):
	cpu=psutil.cpu_times()
	memoria=psutil.virtual_memory()
	network=psutil.net_io_counters(pernic=True)
	#{{'cpu':cpu}}
	#print cpu
	#return render_to_response('sistema/cpu.html', context_instance = RequestContext(request)) ## este es para tener los estilos 
	return render(request, 'sistema/cpu.html', {'cpu':cpu , 'memoria':memoria, 'network':network })


#class cpu(TemplateView):
	
#	def post(self, request, *args, **kwargs):
#		cpu=psutil.virtual_memory()
#		print cpu
#		return render(request,'sistema/cpu.html', {'cpu':cpu})
"""
		buscar = request.POST['buscalo']
		libros = Libro.objects.filter(nombre__contains=buscar)
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
"""