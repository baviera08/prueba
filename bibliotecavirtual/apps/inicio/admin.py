from django.contrib import admin
from .models import usuario, Perfiles, equipo, juego, lobby, rol, permiso, invitacion

admin.site.register(Perfiles)


class usuarioAdmin(admin.ModelAdmin):
	list_display = ('username' ,'email' , 'bloqueado' , 'enlinea')
	list_filter = ('username',)
	search_fields = ('username' , 'nombre')
	#list_editable = ('username' , 'nombre')
	#filter_horizontal = ('autor',)

	#def imagen_portadas(self, libro):
	#	url = libro.traer_url_portadas()
	#	tag = "<img src='%s' >" % url
	#	return tag

	#imagen_portadas.allow_tags = True

admin.site.register(usuario, usuarioAdmin)

class equipoAdmin(admin.ModelAdmin):
	list_display = ('id_equipo' ,'equipo' )#, 'usuario_x_equipo' )
	list_filter = ('equipo',)
	search_fields = ('id_equipo' , 'equipo')
	#list_editable = ('username' , 'nombre')
	#filter_horizontal = ('autor',)


admin.site.register(equipo, equipoAdmin)
admin.site.register(juego)
admin.site.register(lobby)
admin.site.register(rol)
admin.site.register(permiso)
admin.site.register(invitacion)
