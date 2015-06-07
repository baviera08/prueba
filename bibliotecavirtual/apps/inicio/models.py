from django.db import models
from django.contrib.auth.models import User

class Perfiles(models.Model):
	usuario = models.OneToOneField(User)
	telefono = models.IntegerField()

	def __unicode__(self):
		return self.usuario.username

class usuario(models.Model):
    username = models.CharField(max_length=50, default= 'DEFAULT VALUE',  primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email =  models.EmailField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=50)
    '''imagen_perfil = models.ImageField(upload_to = 'fotos_perfiles')'''
    bloqueado = models.BooleanField( default=False)
    enlinea = models.BooleanField( default=False)
 
    def __unicode__(self):
        return self.username

class lobby(models.Model):
    id_lobby= models.IntegerField(primary_key=True)
    nombre= models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre


class juego(models.Model):
    id_juego = models.IntegerField(default=0, primary_key=True)
    id_lobby = models.ForeignKey(lobby, blank=True, null=True)# aca le puse porque me decia que no podia pasarle un valor no nulo a equipo
    nivel= models.IntegerField()
    tiempo_por_turno= models.IntegerField()
    cantidad_jugadores= models.IntegerField()
    marcador_blanco= models.IntegerField()
    marcador_rojo= models.IntegerField()
    terminado= models.BooleanField( default=False)


class equipo(models.Model):
    id_equipo = models.IntegerField(default=0,primary_key=True)
    id_juego = models.ForeignKey('juego', blank=True, null=True)# aca le puse porque me decia que no podia pasarle un valor no nulo a equipo
    usuario_x_equipo = models.ManyToManyField(usuario)
    equipo = models.CharField(max_length=50, unique=True)
 
    def __unicode__(self):
        return self.equipo

class rol(models.Model):
    id_rol= models.IntegerField(primary_key=True)
    rol=models.CharField(max_length=50)
    usuario_x_rol=models.ManyToManyField(usuario)

    def __unicode__(self):
        return self.rol

class permiso(models.Model):
    id_permiso= models.IntegerField(primary_key=True)
    descripcion=models.CharField(max_length=100)
    rol_x_permiso=models.ManyToManyField(rol)       

    def __unicode__(self):
        return self.descripcion

class invitacion(models.Model):
    id_invitacion=models.IntegerField(primary_key=True)
    mensaje=models.CharField(max_length=100)
    remitente=models.ForeignKey(usuario, blank=True, null=True)
    destinatario=models.ManyToManyField(usuario , related_name="destinatario")
    

    def __unicode__(self):
        return self.id_invitacion